from typing import *

class Timestamp:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    @classmethod
    def process(cls, time):
        if isinstance(time, Timestamp):
            return time

        try:
            time_frame = [int(x) for x in time.split(':')]
            return cls(*time_frame)
        except:
            raise ValueError(f"Invalid timestamp value: {time}")

    def _get_absolute_minutes(time):
        return time.hour * 60 + time.minute

    def __repr__(self):
        return f"{self.hour}:{self.minute}"

    def __sub__(self, other):
        start = other._get_absolute()
        stop = self._get_absolute_minutes()

        return Timestamp(*divmod(stop-start, 60))

    def __lt__(self, other):
        if self.hour == other.hour:
            return self.minute < other.minute
        return self.hour < other.hour

    def __gt__(self, other):
        if self.hour == other.hour:
            return self.minute > other.minute
        return self.hour > other.hour


class Timeframe:
    def __init__(self, start, stop):
        self.start = Timestamp.process(start)
        self.stop = Timestamp.process(stop)

    def to_list(self):
        start = f"{self.start.hour}:{self.start.minute if self.start.minute else '00'}"
        stop = f"{self.stop.hour}:{self.stop.minute if self.stop.minute else '00'}"
        return [start, stop]

    def __repr__(self):
        return f"({self.start} - {self.stop})"

    def __contains__(self, time):
        start = self.start._get_absolute_minutes()
        stop = self.stop._get_absolute_minutes()
        return start < time._get_absolute() < stop

    def time_delta(self):
        start = self.start._get_absolute_minutes()
        stop = self.stop._get_absolute_minutes()
        return stop - start

    def __and__(self, other):
        a_start = self.start._get_absolute_minutes()
        a_stop = self.stop._get_absolute_minutes()

        b_start = other.start._get_absolute_minutes()
        b_stop = other.stop._get_absolute_minutes()

        time_frame = Timeframe(
                Timestamp(*divmod(max(a_start, b_start), 60)),
                Timestamp(*divmod(min(a_stop, b_stop), 60))
            )

        if time_frame.time_delta() > 0:
            return time_frame

class Solution:

    @staticmethod
    def get_user_slots(time_frames, time_bound):
        day_start = Timestamp.process(time_bound[0])
        day_stop = Timestamp.process(time_bound[1])
        avaiable_slots = []

        if Timestamp.process(time_frames[0][0]) > day_start:
            time_frame = Timeframe(day_start, time_frames[0][0])
            avaiable_slots.append(time_frame)

        for cursor in range(len(time_frames) -1):
            time_frame = Timeframe(
                    time_frames[cursor][1],
                    time_frames[cursor+1][0]
                )
            if time_frame.time_delta() > 0:
                avaiable_slots.append(time_frame)

        if Timestamp.process(time_frames[-1][1]) < day_stop:
            time_frame = Timeframe(time_frames[-1][-1], day_stop)
            avaiable_slots.append(time_frame)

        return avaiable_slots

    def compare_two_calendars(self, a:List[Timeframe], b:List[Timeframe]) -> List[Timeframe]:

        possible_slots = []

        for i in a:
            for j in b:
                (i & j) and possible_slots.append(i & j)
        return possible_slots


    def get_available_slots(self, a, a_bound, b, b_bound, required_slot):

        # get all the available slots throughout the day
        avail_a = self.get_user_slots(a, a_bound)
        avail_b = self.get_user_slots(b, b_bound)


        # remove the time frames that are less than required minutes
        avail_a = [frame for frame in avail_a if frame.time_delta() >= required_slot]
        avail_b = [frame for frame in avail_b if frame.time_delta() >= required_slot]

        if not any([avail_a, avail_b]):
            return []

        data = self.compare_two_calendars(avail_a, avail_b)
        return [timeframe.to_list() for timeframe in data]


a = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
a_bound = ['9:00', '20:00']

b = [['10:00', '11:30'], ['12:30','14:30'], ['14:30','15:00'], ['16:00', '17:00']]
b_bound = ['10:00', '18:30']

required_slot = 60

output = [['11:30','12:00'], ['15:00','16:00'], ['18:00', '18:30']]

response = Solution().get_available_slots(a, a_bound, b, b_bound, required_slot)
print(response)
