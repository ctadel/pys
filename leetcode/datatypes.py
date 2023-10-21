from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


    @classmethod
    def from_iterator(cls, iterable):
        output = cls()
        cursor = output

        for item in iterable:
            cursor.next = ListNode(item)
            cursor = cursor.next

        return output.next


    def to_iterator(self):
        output = []
        while(self):
            output.append(str(self.val))
            self = self.next
        return output


    def __str__(self):
        return ' -> '.join(self.to_iterator())



class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def insert(self, node):

        if not isinstance(node, BinaryTreeNode):
            node = BinaryTreeNode(node)

        if node.value < self.value:
            if not self.left:
                self.left = node
            else:
                self.left.insert(node)

        elif node.value > self.value:
            if not self.right:
                self.right = node
            else:
                self.right.insert(node)

        return self

    @classmethod
    def from_iterator(cls, data, root=None):

        def get_element():
            for element in data:
                yield element

        tree = cls(root if root else next(get_element()))

        for element in get_element():
            tree.insert(element)

        return tree


    def __str__(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)
        return ''


    def _display_aux(self):
        """ Copied from stackoverflow """

        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
