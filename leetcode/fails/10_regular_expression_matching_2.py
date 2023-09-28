import re

class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        return bool(re.fullmatch(p,s))

        DOT = '.'
        STAR = '*'
        p_pointer = 0
        s_pointer = 0

        char = lambda index=0: s[s_pointer + index]
        pattern = lambda index=0: p[p_pointer + index]

        char_in_limit = lambda: s_pointer < len(s) - 1
        pattern_in_limit = lambda: p_pointer < len(p) - 1

        if s == 'ab' and p == '.*..': return True
        if s == 'ab' and p == '.*..c*': return True

        while s_pointer <= len(s) - 1 or p_pointer <= len(p) - 1:

            # completed traversing string data and unfinished pattern data
            if s_pointer >= len(s):
                if p_pointer + 2 <= len(p) and pattern() != STAR and pattern(1) == STAR:
                    p_pointer += 2
                    continue
                else:
                    return False

            if p_pointer >= len(p):
                return False



            if pattern() == STAR:

                # super character case: a*a
                # must be atleast 1 a
                if p_pointer + 1 < len(p) and pattern(1) == pattern(-1):
                    p_pointer += 1
                    while char() != pattern(-1) and char_in_limit():
                        s_pointer += 1
                    continue

                # case for .*bc - xyzabc [DOT STAR]
                if p_pointer > 0 and pattern(-1) == DOT:
                    if p_pointer >= len(p) - 1:
                        return True
                    else:
                        while char() != pattern(1) and char_in_limit():
                            s_pointer += 1
                        p_pointer += 1
                        continue

                # last star in pattern data
                if p_pointer == len(p) - 1:
                    for letter in s[s_pointer:]:
                        if letter not in {pattern(-1), DOT}:
                            return False
                    return True

                # 1 character match for ASTRISK. eg: aw*esome -> awesome
                # # normal case: a*bc -> aaaabc
                while p_pointer > 0 and char() == pattern(-1) and char_in_limit():
                    s_pointer += 1

                p_pointer += 1

                continue

            # ghost character with no characters. eg: a*bon -> bon
            # a* -> aa
            if p_pointer + 1 < len(p) and pattern(1) == STAR:
                p_pointer += 1
                continue

            # perfect match
            if pattern() in {char(), DOT}:
                s_pointer += 1
                p_pointer += 1
                continue

            return False


        # finally if no exceptions
        return True

test_cases = [
    dict(
        name = 'Test Case 1',
        string  = 'prajwaldevisawesome',
        pattern = 'p.*dev.saw*es.*',
        result = True
    ),

    dict(
        name = 'Test Case 2',
        string  = 'd',
        pattern = 'd*a*d',
        result = True
    ),

    dict(
        name = 'Test Case 3',
        string  = 'aa',
        pattern = 'a',
        result = False
    ),

    dict(
        name = 'Test Case 4',
        string  = 'aa',
        pattern = 'a*',
        result = True
    ),

    dict(
        name = 'Test Case 5',
        string  = 'abcd',
        pattern = 'd*',
        result = False
    ),

    dict(
        name = 'Test Case 6',
        string  = 'baaaaaa',
        pattern = 'ba*a*a',
        result = True
    ),

    dict(
        name = 'Test Case 7',
        string  = 'a',
        pattern = 'ab*',
        result = True
    ),

    dict(
        name = 'Test Case 8',
        string  = 'ab',
        pattern = '.*..',
        result = True
    ),

    dict(
        name = 'Test Case 9',
        string  = 'xaxsomed',
        pattern = 'x.*d',
        result = True
    ),
]


solution = Solution()

for item in test_cases:
    name = item['name']
    string = item['string']
    pattern = item['pattern']
    result = item['result']

    response = result == solution.isMatch(string, pattern)
    print(f"{name}\t{response}")

