class Solution(object):
    def findPeakElement(self, nums):
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[mid + 1]:
                high = mid
            else:
                low = mid + 1
        return low

obj = Solution()
test_cases = [[1,2,3,1], [1,2,1,3,5,6,4]]
for i in test_cases:
    print(obj.findPeakElement(i))