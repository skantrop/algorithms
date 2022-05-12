from collections import Counter

class Solution(object):
    def divideArray(self, nums):
        return all(i % 2 == 0 for i in Counter(nums).values())
        
obj = Solution()
print(obj.divideArray([3,2,3,2,2,2]))
print(obj.divideArray([1,2,3,4]))