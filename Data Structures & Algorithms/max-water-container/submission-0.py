class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area= 0

        i=0
        j= len(heights) -1

        while i < j:
            diff = j-i
            total = min([heights[i], heights[j]])* diff
            max_area= max(max_area, total)

            if heights[i] < heights[j]:
                i +=1
            else:
                j -= 1
                
        return max_area