class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = len(word1), len(word2)
        sentence = ''
        for i,j in zip(word1, word2):
            sentence += i + j

        if l1 > l2:
            return sentence + word1[l2:]
        return sentence + word2[l1:]

word1 = 'prajwal'
word2 = 'dev'
result = Solution().mergeAlternately(word1, word2)
print(result)
