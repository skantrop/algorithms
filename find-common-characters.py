class Solution(object):
    def commonChars(self, words):
        prev = list(words[0])
        for word in words:
            chars_count = {}
            res = []
            for i in prev:
                if i in chars_count:
                    chars_count[i] += 1
                else:
                    chars_count[i] = 1
            for i in word:
                if i not in chars_count:
                    continue
                elif i in chars_count and chars_count[i] != 0:
                    chars_count[i] -= 1
                    res.append(i)
            prev = res
        return prev

obj = Solution()
test_cases = [["bella","label","roller"], ["cool","lock","cook"]]
for i in test_cases:
    print(obj.commonChars(i))
