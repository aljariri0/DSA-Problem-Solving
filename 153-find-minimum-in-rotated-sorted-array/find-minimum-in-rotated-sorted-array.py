class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1
        answer = nums[0]

        while l <= r:

            if nums[l] <= nums[r]:
                answer = min(answer, nums[l])
                break

            m = (l + r) // 2
            answer = min(nums[m], answer)

            if nums[m] >= nums[l]:
                l = m + 1

            else:
                r = m - 1

        return answer

