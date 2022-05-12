class Solution(object):
    def nextGreatestLetter(self, letters, target):
        low = 0
        high = len(letters) - 1 
    
        while low <= high :            
            mid = (low+high)//2
        
            if letters[mid] > target :
                high = mid -1 
            elif letters[mid] <=  target :
                low = mid + 1 
        
        if low > len(letters) - 1 :
            return letters[0]
        
        return letters[low]

obj = Solution()
test_cases = [(["c","f","j"], "a"),
(["c","f","j"], "c"), (["c","f","j"], "d"), (["c","f","j"], "j"), ]

for i, j in test_cases:
    print(obj.nextGreatestLetter(letters=i, target=j))
