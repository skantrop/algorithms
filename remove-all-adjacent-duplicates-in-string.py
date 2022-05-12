class Solution(object):
    def removeDuplicates(self, s):
        seen=[]
        for i,j in enumerate(s) :
            if seen and seen[-1]== j :
                seen.pop()
            else :
                seen.append(j)    
        return ''.join(seen)        
            
obj = Solution()
print(obj.removeDuplicates(s = "abbaca"))
print(obj.removeDuplicates(s = "azxxzy"))
