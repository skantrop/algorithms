class Solution:
    def maxPairs(self, nums, k):
        nums = sorted(nums)
        count = 0
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] > k:
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                left += 1
                right -= 1
                count += 1
        return count
obj = Solution()
print(obj.maxPairs(nums = [1,2,3,4], k = 5))
print(obj.maxPairs(nums = [3,1,3,4,3], k = 6))
