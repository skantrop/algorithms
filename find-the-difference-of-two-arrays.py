class Solution(object):
    def findDifference(self, nums1, nums2):
        s1 = set(nums1)
        s2= set(nums2)
        res = []
        res.append(list(s1.difference(s2)))
        res.append(list(s2.difference(s1)))
        return res
        
obj = Solution()
print(obj.findDifference(nums1 = [1,2,3], nums2 = [2,4,6]))
print(obj.findDifference(nums1 = [1,2,3,3], nums2 = [1,1,2,2]))