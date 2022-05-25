class Solution:
    def threeSumClosest(self, nums, target):
        final = float('inf')
        for i in range(len(nums)-1):
            for j in range(len(nums)-1-i):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]

        for i in range(len(nums)-2):
            low = i+1
            high = len(nums)-1

            while low < high:
                sum_ = sum([nums[i],nums[low],nums[high]])
                difft = abs(target-sum_)
                if difft< final:
                    final = difft
                    res = sum_
                if sum_< target:
                    low = low+1
                elif sum_ > target:
                    high = high-1
                else:
                    return res
        return res

obj = Solution()
print(obj.threeSumClosest(nums = [-1,2,1,-4], target = 1))
print(obj.threeSumClosest(nums = [0,0,0], target = 1))

                   