class Solution(object):
    def intersect(self, nums1, nums2):
        res = []
        nums1.sort()
        nums2.sort()
        i = 0 
        j = 0
        while i < len(nums1) and j < len(nums2):
            print('i', nums1[i])
            print('j', nums2[j])
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res += nums1[i],
                i += 1
                j += 1
        return res

obj = Solution()
print(obj.intersect([1,2,2,1], [2,2]))
print(obj.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))