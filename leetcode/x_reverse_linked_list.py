from datatypes import ListNode

class Solution:

    def reverse_linked_list(self, head:ListNode) -> ListNode:
        past = None

        while head:
            future = head.next
            head.next = past

            head, past = future, head

        return past

data = ListNode.from_iterator(list('9842408136'))
print(data)

response = Solution().reverse_linked_list(data)
print(response)
