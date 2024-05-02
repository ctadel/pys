from datatypes import BinaryTreeNode as BST

class Solution:

    def findInOrderSuccessor(self, node:BST, target, successor=float('inf')) -> int:

        if not node:
            return successor

        if successor > node.value > target:
            successor = node.value

        if node.value > target:
            return self.findInOrderSuccessor(node.left, target, successor)
        else:
            return self.findInOrderSuccessor(node.right, target, successor)


tree = BST.from_iterator([85, 60, 2, 24, 65, 87, 9, 3, 47, 54, 50, 78, 19, 42, 56, 21, 1, 131, 139, 124, 123, 125, 149, 111, 90, 133, 108])
print(tree)

result = Solution().findInOrderSuccessor(tree, 123)
print(result)
