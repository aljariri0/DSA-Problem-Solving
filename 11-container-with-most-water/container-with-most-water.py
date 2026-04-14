class Solution:
    def maxArea(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1
        mAmount = float("-inf") 


        while l < r:
            
            area = (r - l) * min(height[l], height[r])
            mAmount = max(mAmount, area)

            if height[l] < height[r]:
                l += 1

            elif height[l] > height[r]:
                r -= 1

            else:
                r -= 1
                l += 1

        return mAmount