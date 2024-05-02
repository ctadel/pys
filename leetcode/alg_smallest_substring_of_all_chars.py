class Solution:
    def get_smallest_substring(self, string:str, chars:list[str]) -> str:

        i, j = 0, len(chars)
        substring = slice(0, len(string))
        while i < j and j < len(string):
            if set(chars).issubset(set(string[i:j])) and len(string[i:j]) < len(string[substring]):
                substring = slice(i,j)

            if string[i] == string[j] or string[i] not in chars:
                i += 1

            j += 1

        return string[substring]


result = Solution().get_smallest_substring('prajwaldevisdogshit', list('dig'))
print(result)
