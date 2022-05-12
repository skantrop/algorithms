class Solution(object):
    def frequencySort(self, nums):
        seen = {} # storing key -> number of frequency: value -> number
        res = []
        for i in set(nums):
            freq = nums.count(i)
            if freq not in seen:
                seen[freq] = [i]
            else:
                seen[freq].append(i)
        for i in sorted(seen):
            for j in sorted(seen[i], reverse=True): #case of dcr order
                res.extend([j]*i)
        return res

obj = Solution()
test_cases = [[1,1,2,2,2,3], [2,3,1,3,2], [-1,1,-6,4,5,-6,1,4,1]]
for i in test_cases:
    print(obj.frequencySort(i))