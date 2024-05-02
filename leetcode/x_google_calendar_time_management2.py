class Timestamp:
    def __init__(self, hour:int, minute:int):
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        return f"{self.hour}:{self.minute}"

    @classmethod
    def from_string(cls, time_string:str):
        return cls(*[int(x) for x in time_string.split(':')])

    def to_int(self):
        return self.hour * 60 + self.minute

    @classmethod
    def from_int(cls, value):
        return cls(*divmod(value, 60))

    @staticmethod
    def minimum(*timestamps):
        return min(timestamps, key=lambda x: x.to_int())

    @staticmethod
    def maximum(*timestamps):
        return max(timestamps, key=lambda x: x.to_int())

    def __le__(self, other):
        if self.hour == other.hour:
            return self.minute <= other.minute
        return self.hour <= other.hour

    def __lt__(self, other):
        if self.hour == other.hour:
            return self.minute < other.minute
        return self.hour < other.hour

    def __ge__(self, other):
        if self.hour == other.hour:
            return self.minute >= other.minute
        return self.hour >= other.hour

    def __ge__(self, other):
        if self.hour == other.hour:
            return self.minute >= other.minute
        return self.hour >= other.hour

    def __add__(self, other):
        if isinstance(other, Timestamp):
            return Timestamp.from_int(self.to_int() + other.to_int())
        elif isinstance(other, int):
            return Timestamp.from_int(self.to_int() + other)
        else:
            raise TypeError("Invalid type of value: ", other)

    def __sub__(self, other):
        if isinstance(other, Timestamp):
            return Timestamp.from_int(self.to_int() - other.to_int())
        elif isinstance(other, int):
            return Timestamp.from_int(self.to_int() - other)
        else:
            raise TypeError("Invalid type of value: ", other)



class Timeframe:
    def __init__(self, start:Timestamp, stop:Timestamp):
        self.start = start
        self.stop = stop

    @classmethod
    def from_list(cls, time_frame:list):
        start = Timestamp.from_string(time_frame[0])
        stop = Timestamp.from_string(time_frame[1])
        return cls(start, stop)

    def __contains__(self, value:Timestamp):
        return self.start.to_int() < value.to_int() < self.stop.to_int()

    def __repr__(self):
        return f"({self.start} - {self.stop})"



class Solution:
    def get_available_slots(self, a, a_bound, b, b_bound, required_slot):
        a = [Timeframe.from_list(t) for t in a]
        b = [Timeframe.from_list(t) for t in b]

        all_available_slots = []

        common_day_start = Timestamp.maximum(
                Timestamp.from_string(a_bound[0]),
                Timestamp.from_string(b_bound[0])
            )

        common_day_end  = Timestamp.minimum(
                Timestamp.from_string(a_bound[1]),
                Timestamp.from_string(b_bound[1])
            )


        # pointer = common_day_start
        # l = r = 0
        # while l<len(a) or r<len(b):
        #     next_frame = Timestamp.minimum(a[l].start, b[r].start)
        #     delta = next_frame - pointer

        #     if delta.to_int() >= required_slot:
        #         all_available_slots.append(
        #                 Timeframe(pointer, next_frame)
        #             )

        #     pointer = Timestamp.maximum(a[l].stop, b[r].stop)

        #     if a[l].stop <= b[r].stop or a[l].stop <= pointer and l<len(a)-1:
        #         l += 1
        #     if b[r].stop <= a[l].stop or a[l].stop <= pointer and r<len(b)-1:
        #         r += 1

        l = r = 0
        merged_busy_slots = []
        while l<len(a) and r<len(b):
            try:
                x = a[l]
            except IndexError:
                merged_busy_slots.extend(b[r:])
                break

            try:
                y = b[r]
            except IndexError:
                merged_busy_slots.extend(a[l:])
                break

            start = Timestamp.minimum(x.start, y.start)
            stop = Timestamp.maximum(x.stop, y.stop)
            print(start, stop)
            merged_busy_slots.append(Timeframe(start,stop))

            if x.stop < y.stop:
                l += 1
            elif y.stop < x.stop:
                r += 1
            else:
                a += 1
                r += 1

        return merged_busy_slots


a = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
b = [['10:00', '11:30'], ['12:30','14:30'], ['14:30','15:00'], ['16:00', '17:00']]

a_bound = ['9:00', '20:00']
b_bound = ['10:00', '18:30']

required_slot = 20

output = [['11:30','12:00'], ['15:00','16:00'], ['18:00', '18:30']]

response = Solution().get_available_slots(a, a_bound, b, b_bound, required_slot)
print(response)

