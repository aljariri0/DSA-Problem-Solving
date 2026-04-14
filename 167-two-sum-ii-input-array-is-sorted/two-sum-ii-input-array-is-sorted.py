class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        result = []
        s = 0

        l = 0
        r = len(numbers) - 1


        while l < r:

            s = numbers[l] + numbers[r]

            if s > target:
                r -= 1

            elif s < target:
                l += 1

            else:

                result.append(l + 1)
                result.append(r + 1)
                l += 1
                r -= 1

        return result