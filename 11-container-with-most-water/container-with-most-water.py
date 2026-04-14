class Solution:
    def maxArea(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1
        mAmount = float("-inf") 


        for i in range(len(height)):

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