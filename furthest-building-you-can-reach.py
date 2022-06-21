import heapq
class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        heap = []
        
        for i in range(len(heights)-1):
            j = i+1
            diff = heights[j] - heights[i]
            
            if diff <= 0:
                continue
            
            if diff > 0:
                heapq.heappush(heap, diff)
                # print(heap)
            
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
                print(heapq.heappop(heap))
            
            if bricks < 0:
                return i
        return len(heights)-1

obj = Solution()
print(obj.furthestBuilding(heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1))