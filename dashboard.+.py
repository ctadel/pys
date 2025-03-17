#!/usr/bin/env python3
import base64

dashbaord = {
        'Lights': {'entity_id':'switch.prajwal_s_4_touch_switch_switch_3', 'icon':'/home/prajwal/.local/share/icons/ha/bulb.png'},
        'Fans': {'entity_id':'switch.prajwal_s_4_touch_switch_switch_4', 'icon':'/home/prajwal/.local/share/icons/ha/fan.png'},
        '2-pin Socket': {'entity_id':'switch.prajwal_s_4_touch_switch_switch_1', 'icon':'/home/prajwal/.local/share/icons/ha/2-pin socket.png'},
        '3-pin Socket': {'entity_id':'switch.prajwal_s_4_touch_switch_switch_2', 'icon':'/home/prajwal/.local/share/icons/ha/3-pin socket.png'},
}

import urllib.request
import json

HA_URL = "http://localhost:8123/api/states"
HA_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI2ZTUzMzZiNGQ5OGE0M2I5YWY4M2I1MDY3M2EzOTVlZCIsImlhdCI6MTczNzExNTU2OCwiZXhwIjoyMDUyNDc1NTY4fQ.5XQFT0_z68xGhHTOVspMJghFKk5U5x_bK2Z_mqkpVIw"

headers = {"Authorization": f"Bearer {HA_TOKEN}", 'Content-Type': 'application/json'}

req = urllib.request.Request(HA_URL, headers=headers)
with urllib.request.urlopen(req) as response:
    states = json.loads(response.read().decode())

entities_ids = {entity['entity_id']:device for device,entity in dashbaord.items()}
entities_states = {entities_ids[ent['entity_id']]:False if ent['state'] == 'off' else True for ent in states if ent['entity_id'] in entities_ids.keys()}
for name, state in entities_states.items():
    dashbaord[name]['state'] = state


print("🏛\n---")

for category, details in dashbaord.items():
    icon = details['icon']
    try:
        with open(icon, 'rb') as image_file:
            icon_base64 = base64.b64encode(image_file.read()).decode('utf-8')
    except:
        icon_base64 = ''

    color = 'green' if details['state'] else 'grey'
    span = f"‎<b><span color='{color}'>{category}</span></b>"
    print(f" {span}| image='{icon_base64}' imageWidth=20")

    action = 'off' if details['state'] else 'on'
    command = f"/usr/bin/ha {details['entity_id']} {action}"
    print(f"-- Switch {action} | useMarkup=false bash='{command}' terminal=false")
