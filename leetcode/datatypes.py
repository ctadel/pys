from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


    @classmethod
    def from_iterable(cls, iterable):
        output = cls()
        cursor = output

        for item in iterable:
            cursor.next = ListNode(item)
            cursor = cursor.next

        return output.next


    def to_iterable(self):
        output = []
        while(self):
            output.append(str(self.val))
            self = self.next
        return output


    def __str__(self):
        return ' -> '.join(self.to_iterable())

