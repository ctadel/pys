from typing import *
from itertools import product
from utils import time_it

class Solution:
    MAPPER = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz',
        }

    @time_it
    def method_backtrack(self, digits: str) -> List[str]:
        n = len(digits)
        res = []
        letters = {'2':['a','b','c'] , '3':['d','e','f'] , '4':['g','h','i'] , '5':['j','k','l'] , '6':['m','n','o'] , '7':['p','q','r','s'] , '8':['t','u','v'], '9':['w','x','y','z']}

        def backTrack(temp,index):
            if len(temp) == n:
                return temp

            for j in letters[digits[index]]:
                temp += j
                a = backTrack(temp, index+1)
                if a:
                    res.append(a)
                temp = temp[0:-1]

        backTrack('',0)

        return res

    @time_it
    def method_pythonic(self, digits: str) -> List[str]:

        if not digits: return []
        data = product(*[self.MAPPER[d] for d in digits if d in self.MAPPER])
        return [''.join(datum) for datum in data]



    @time_it
    def method_me(self, digits: str) -> List[str]:

        final, temp = [''], []
        for digit in digits:
            for letter in self.MAPPER[digit]:
                for each in final:
                    temp.append(each+letter)

            final, temp = temp, []

        return final

num = '98424834324523'
data = Solution().method_pythonic(num)
print(len(data))

data = Solution().method_backtrack(num)
print(len(data))

data = Solution().method_me(num)
print(len(data))

