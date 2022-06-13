class Solution:
    def maximumUniqueSubarray(self, nums):
        res=0
        count=0
        seen=set()
        pointer=0
        for i in range(len(nums)):
            while nums[i] in seen:
                seen.remove(nums[pointer])
                count=count-nums[pointer]
                pointer=pointer+1
            seen.add(nums[i])
            count=count+nums[i]
            res=max(res,count)
        return res
obj = Solution()
test_cases = [[4,2,4,5,6], ]
for i in test_cases:
    print(obj.maximumUniqueSubarray(nums=i))

