
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        STAR = '*'
        DOT = '.'

        string = s[::-1]
        pattern = p[::-1]

        while string or pattern:

            if string[-1] != STAR and string[-1] not in {pattern[-1], DOT}:
                return False

            if string[-1] == STAR:
                wildcard = string[-2]
                if wildcard == STAR: return False
                string = string[:-2]

                if wildcard == DOT:
                    ...

                else:
                    while string[-1] == wildcard:
                        string = string[:-1]


            else:
                string = string[:-1]
                pattern = pattern[:-1]

        return True
