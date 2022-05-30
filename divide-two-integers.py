class Solution(object):
    def divide(self, dividend, divisor):
        negative = False
        
        if dividend > 0  and divisor < 0 or dividend < 0 and divisor > 0:
            negative = True

        if dividend < 0:
            dividend = -dividend

        if divisor < 0:
            divisor = -divisor        
        
        res = 0
        
        while dividend >= divisor:
            dummy = divisor
            
            count = 1
            
            while dividend >= dummy:
                dividend -= dummy
                res += count
                
                count <<= 1
                dummy <<= 1
        if negative:
            res = -res
        if res >= 2 ** 31:
            res = (2 ** 31) - 1        
        return res

obj = Solution()
test_cases = [[10,3], [7, -3]]
for i, j in test_cases:
    print(obj.divide(i, j))


