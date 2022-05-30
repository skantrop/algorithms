# class Solution:
#     def threeSumClosest(self, nums, target):
#         final = float('inf')
#         for i in range(len(nums)-1):
#             for j in range(len(nums)-1-i):
#                 if nums[j]>nums[j+1]:
#                     nums[j],nums[j+1] = nums[j+1],nums[j]

#         for i in range(len(nums)-2):
#             low = i+1
#             high = len(nums)-1

#             while low < high:
#                 sum_ = sum([nums[i],nums[low],nums[high]])
#                 difft = abs(target-sum_)
#                 if difft< final:
#                     final = difft
#                     res = sum_
#                 if sum_< target:
#                     low = low+1
#                 elif sum_ > target:
#                     high = high-1
#                 else:
#                     return res
#         return res

# obj = Solution()
# print(obj.threeSumClosest(nums = [-1,2,1,-4], target = 1))
# print(obj.threeSumClosest(nums = [0,0,0], target = 1))



###############################
#SECOND SOLUTION
class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        close = []
        for i in range(0, nums.__len__()-2):
            j, k = i+1, nums.__len__()-1
            if nums[i]+nums[k-1]+nums[k] < target:
                close.append(nums[i]+nums[k-1]+nums[k])
            elif nums[i]+nums[j]+nums[j+1] > target:
                close.append(nums[i]+nums[j]+nums[j+1])
            else:
                while j < k:
                    temp = nums[i]+nums[j]+nums[k]
                    if temp == target:
                        return temp
                    close.append(temp)
                    if temp < target:
                        j += 1
                    else:
                        k -= 1
        closest = sorted(close, key=lambda x: abs(target-x))
        return closest[0]

obj = Solution()
print(obj.threeSumClosest(nums = [-1,2,1,-4], target = 1))
print(obj.threeSumClosest(nums = [0,0,0], target = 1))
