class Solution(object):
    def arrangeCoins(self, n):
        low = 1
        high = n
        while low <= high:
            mid = low + (high - low) // 2
            needed = mid * (mid + 1) // 2
            if needed == n:
                return mid
            elif needed < n:
                low = mid + 1
            else:
                high = mid - 1

        return high
obj = Solution()
test_cases = [5,8,9]
for i in test_cases:
    print(obj.arrangeCoins(i))