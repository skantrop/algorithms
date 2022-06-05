from math import sqrt
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:   return 0
        arr = [0, 0] + [1] * (n-2)
        start = 2
        while start < sqrt(n):
            if arr[start] == 1:
                arr[start*start : n : start] = [0] * (1 + (n - start*start - 1) // start) 
            start += 2 if start != 2 else 1
        return sum(arr)
obj = Solution()
test_cases = [10, 0, 1]
for i in test_cases:
    print(obj.countPrimes(i))