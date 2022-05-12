import collections
class Solution(object):
    def groupThePeople(self, groupSizes):
        groups = collections.defaultdict(list)
        res = []
        for i, j in enumerate(groupSizes):
            groups[j].append(i)
            if len(groups[j]) == j:
                res.append(groups.pop(j))
        return res

obj1 = Solution()
print(obj1.groupThePeople([1,3,3,3,3,3,3]))
print(obj1.groupThePeople([2,1,3,3,3,2]))


class Solution(object):
    def groupThePeople(self, groupSizes):
        groups = {}
        res = []
        for id in range(len(groupSizes)):
            group_size = groupSizes[id]
            if group_size not in groups:
                groups[group_size] = [[id]] # add key with value if there's not more el left
            else:
                # if group size if full
                print('groups',groups,  groups[group_size])
                print('el', groups[group_size][-1])
                if len(groups[group_size][-1]) == group_size:
                    groups[group_size].append([id]) # key {el: [array of elements]}
                else:
                    groups[group_size][-1].append(id)
        for i in groups.values():
            res.extend(i)
        return res


obj2 = Solution()
print(obj2.groupThePeople([1,3,3,3,3,3,3]))
print(obj2.groupThePeople([2,1,3,3,3,2]))