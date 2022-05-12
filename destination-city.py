class Solution:
    def destCity(self, paths):
        start = set()
        end = set()

        for i in paths:
            start.add(i[0])
            end.add(i[1])
        print(start)
        print(end)
        return list(end.difference(start))[0]

obj = Solution()
print(obj.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
print(obj.destCity([["B","C"],["D","B"],["C","A"]]
))
print(obj.destCity([["A","Z"]]))