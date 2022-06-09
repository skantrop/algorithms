class Solution:
    def findRestaurant(self, list1, list2):
        seen={}
        for i in list1:
            for j in list2:
                if i==j:
                    seen[i]=list1.index(i)+list2.index(j)
        keys=list(seen.values())
        values=list(seen.keys())
        min_idx=min(keys)
        res=[]
        for i in range(len(keys)):
            if min_idx==keys[i]:
                res.append(values[keys.index(keys[i])])
            keys[i]=-1
        return res

obj = Solution()
print(obj.findRestaurant(
["Shogun","Tapioca Express","Burger King","KFC"],
["KFC","Burger King","Tapioca Express","Shogun"]))