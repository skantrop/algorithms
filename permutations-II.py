import itertools

class Solution(object):
    def permuteUnique(self, nums):
        return [i for i in set(itertools.permutations(nums, len(nums)))]

obj = Solution()
test_cases = [[1,1,2], [1,2,3]]
for i in test_cases:
    print(obj.permuteUnique(i))