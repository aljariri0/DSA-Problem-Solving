class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        result = [0] * (len(nums))

        for i in range(len(nums)):

            if (i + k) <= len(nums) - 1:

                result[i + k] = nums[i]

            else:

                result[(i + k) % len(nums)] = nums[i]

        for j in range(len(nums)):

            nums[j] = result[j]
        