import itertools

"""
combinations() method provides with all the possible tuples a sequence or set of numbers or letters used in the iterator and the elements are assumed to be unique on the basis of there positions which are distinct for all elements.
"""
class Solution(object):
    def combinationSum3(self, k, n):
        range_ = range(1, 10)
        combination = itertools.combinations(range_, k)
        res = [list(i) for i in combination if sum(i) == n]
        return res

obj = Solution()
test_cases = [(3, 7), (3,9), (4,1)]

for i, j in test_cases:
    print(obj.combinationSum3(k=i, n=j))