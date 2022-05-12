class Solution(object):
    def removeDuplicates(self, s, k):
        seen = []
        string = ''
        for i in s:
            if seen and seen[-1][0] == i:
                seen[-1][-1] +=1
            else:
                seen.append([i,1])
            if seen[-1][-1] == k:
                seen.pop()
        for i, j in seen:
            string+=i*j
        return string

obj = Solution()
print(obj.removeDuplicates(s = "abcd", k = 2))
print(obj.removeDuplicates(s = "deeedbbcccbdaa", k = 3))
print(obj.removeDuplicates(s = "pbbcggttciiippooaais", k = 2))
