from fastapi import FastAPI
from fastapi.params import Path
from pydantic import BaseModel
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

import uvicorn
import os

app = FastAPI()

API_KEY = "howaboutnothing"

class PasswordInput(BaseModel):
    password: str

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Debugging: Print all headers to check for the presence of X-Auth
        print(f"Request Headers: {request.headers}")

        # Check if the X-Auth header is provided
        x_auth = request.headers.get("X-Auth")

        # If the header is missing or incorrect, raise Unauthorized error
        if x_auth != API_KEY:
            return JSONResponse(status_code=403, content={"detail": "Unauthorized"})

        # Continue processing the request
        response = await call_next(request)
        return response


class HelperFunctions:

    @staticmethod
    def get_user():
        return os.environ.get("USER")  # Get the current username

    @staticmethod
    def get_uid():
        return os.getuid()

    @staticmethod
    def get_user_session_id():
        import subprocess
        user = HelperFunctions.get_user()

        output = subprocess.check_output(["loginctl", "show-user", user, "--property=Sessions"]).decode()
        session_id = output.strip().split("=")[1]
        return session_id

# Add the custom AuthMiddleware to the FastAPI app
app.add_middleware(AuthMiddleware)

@app.post("/shutdown")
async def shutdown():
    os.system("sudo /sbin/shutdown now")
    return {"status": "Shutting down"}

@app.post("/shutdown/{minutes}")
async def shutdown_in(minutes: int):
    os.system(f"sudo /sbin/shutdown +{minutes}")  # shutdown will call systemctl internally
    return {"status": f"Shutdown scheduled in {minutes} minute(s)"}

@app.post("/cancel_shutdown")
async def cancel_shutdown():
    os.system("sudo /sbin/shutdown -c")
    return {"status": "Shutdown canceled"}

@app.post("/logout")
async def logout():
    try:
        user_id = HelperFunctions.get_uid()
    except Exception as e:
        return JSONResponse(
            status_code=404,
            content={
                "message": "There is no ongoing session to logout.",
                }
            )
    os.environ["DISPLAY"] = ":0" #X11 display server
    os.environ["DBUS_SESSION_BUS_ADDRESS"] = f"unix:path=/run/user/{user_id}/bus"
    os.system("gnome-session-quit --logout --no-prompt")
    return {"status": "Logging out"}

@app.post("/lock")
async def lock():
    try:
        session_id = HelperFunctions.get_user_session_id()
    except Exception as e:
        return JSONResponse(
            status_code=404,
            content={
                "message": "There is no ongoing session to lock.",
                }
            )

    os.system(f"loginctl lock-session {session_id}")
    return {"status": "System locked"}

@app.post("/unlock")
async def unlock(body: PasswordInput):
    fail_send_password = os.system(f"DISPLAY=:0 xdotool type '{body.password}'")
    fail_send_return = os.system(f"DISPLAY=:0 xdotool key Return")

    if any([fail_send_password, fail_send_return]):
        return JSONResponse(
                status_code=404,
                content={"message": "No Display manager found to automate"}
            )

    return {"status": "Unlock keystrokes sent"}


if __name__ == "__main__":
    import sys
    from pathlib import Path

    file = Path(sys.argv[0]).name.split('.')[0]
    uvicorn.run(f"{file}:app", host="0.0.0.0", port=6789, reload=True)
