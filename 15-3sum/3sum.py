class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        answer = []
        nums.sort()

        for i, v in enumerate(nums):
            if i > 0 and v == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:

                nSum = nums[i] + nums[l] + nums[r]

                if nSum < 0:
                    l += 1

                elif nSum > 0:
                    r -= 1

                else:

                    answer.append([nums[i], nums[l], nums[r]])
                    l += 1
                     
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    

        return answer