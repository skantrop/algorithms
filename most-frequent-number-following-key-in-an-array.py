class Solution(object):
    def mostFrequent(self, nums, key):
        freq={}
        n=len(nums)
        for i in range(n):
            if nums[i]==key and i+1< n:
                if nums[i+1] in freq:
                    freq[nums[i+1]]+=1
                else:
                    freq[nums[i+1]]=1
        return max(freq, key=freq.get)

obj = Solution()
test_cases = [([1,100,200,1,100], 1), ([2,2,2,2,3], 2) ]
for i, j in test_cases:
    print(obj.mostFrequent(i,j))
