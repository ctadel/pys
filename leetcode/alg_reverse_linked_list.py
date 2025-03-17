from datatypes import ListNode


l = ListNode.from_iterator([1,2,3,4,5,6])
print(l)

def reverse_linked_list(head):
    if not head.next:
        return

def reverse_ll_tp(head):


    prev = None

    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev

print(reverse_ll_tp(l))
