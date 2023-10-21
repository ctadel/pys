from datatypes import BinaryTreeNode

class Solution:
    def reverse_binary_tree(self, root:BinaryTreeNode) -> BinaryTreeNode:

        root.left, root.right = root.right, root.left
        if root.left:
            self.reverse_binary_tree(root.left)
        if root.right:
            self.reverse_binary_tree(root.right)

        return root

data = [4,12,18,5,15,13,51,17,25,31,2,80,21]
root = BinaryTreeNode.from_iterator(data, root=18)
print(root)

Solution().reverse_binary_tree(root)
print(root)
