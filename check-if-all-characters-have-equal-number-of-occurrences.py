class Solution(object):
    def areOccurrencesEqual(self, s):
        freq = [s.count(i) for i in set(s)]
        if len(set(freq)) == 1:
            return True
        else:
            return False
            
        
obj = Solution()
test_cases = ["aaabb", "abacbc"]
for i in test_cases:
    print(obj.areOccurrencesEqual(i))