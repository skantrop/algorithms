class Solution(object):
    def longestValidParentheses(self, s):
        if not s:
            return 0
        valid = 0
        stack=[-1] # initialize with a start index
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack: # if popped -1, add a new start index
                    stack.append(i)
                else:
                    valid=max(valid, i-stack[-1]) # update the length of the valid substring
        return valid

obj = Solution()
test_cases = ["(()", ")()())", ""]
for i in test_cases:
    print(obj.longestValidParentheses(s=i))
