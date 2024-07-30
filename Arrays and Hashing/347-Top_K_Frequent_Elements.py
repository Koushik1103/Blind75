#HashMaps and Heap O(n log n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        heap = []
        for i in nums:
            if i not in d.keys():
                d[i]=1
            else:
                d[i]+=1

        for key, value in d.items():
            heapq.heappush(heap, (-value, key))
        
        l = []
        while len(l)<k:
            l.append(heapq.heappop(heap)[1])

        return l
