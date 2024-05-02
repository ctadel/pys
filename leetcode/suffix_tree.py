class Node:
    def __init__(self, value, index) -> None:
        self.value = value
        self.index = index
        self.indices = {}


    def add_suffix(self, node):
        for tter in node.value:


    @classmethod
    def create_tree(cls, string:str):
        length = len(string)
        tree = Node('\$', length)
        for index in range(1, len(string)):
            tree.add_suffix(
                Node(string[:length-index], length-index)
            )
            print(string[length-index:], length-index)
        return tree

    def locate(self, sub_string:str) -> int:
        return 0


class Solution:
    def get_index_of_substring(self, string:str, sub_string:str) -> int:

        suffix_tree = Node.create_tree(string)
        return suffix_tree.locate(sub_string)


string = 'ishadevisaheroine'
sub_string = 'devisahero'

response = Solution().get_index_of_substring(string, sub_string)
print(response)
