class Solution(object):
    def countAndSay(self, n):
        res = '1'
        for i in range(1, n):
            prev = ''
            count = 0
            dummy = ""
            for j in res:
                if j == prev or prev == '':
                    count += 1
                else:
                    dummy += str(count) + prev
                    count = 1
                prev = j
            dummy += str(count) + prev
            res = dummy
        return res

test_cases = [1,]
obj = Solution()
obj.countAndSay(4)