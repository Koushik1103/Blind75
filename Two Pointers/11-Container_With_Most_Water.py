#Two Pointers O(n)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        areaMax = 0
        first = 0
        last = len(height) - 1
        while first < last:
            area = (last - first) * min(height[last], height[first])
            areaMax = max(areaMax, area)
            if height[first] < height[last]:
                first += 1
            else:
                last -= 1
        return areaMax

