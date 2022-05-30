class Solution(object):
    def maxProduct(self, words):                  
        uniques = [set(words[i]) for i in range(len(words))]                                           
        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not (uniques[i] & uniques[j]):
                    res=max(res, len(words[i]) * len(words[j]))
        return res

obj = Solution()
test_cases = [["abcw","baz","foo","bar","xtfn","abcdef"], ["a","ab","abc","d","cd","bcd","abcd"], ["a","aa","aaa","aaaa"]]
for i in test_cases:
    print(obj.maxProduct(i))
