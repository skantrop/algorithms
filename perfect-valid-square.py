class Solution(object):
    def isPerfectSquare(self, num):
        left = 0
        right = num
        while left <= right:
            mid = (left + right) // 2
            if mid**2 < num:
                left = mid + 1
            elif mid**2 > num:
                right = mid - 1
            else:
                return True
        return False
obj = Solution()
test_cases = [16,14,23,25]
for i in test_cases:
    print(obj.isPerfectSquare(i))
