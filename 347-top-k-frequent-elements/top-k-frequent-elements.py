class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # test

        result = {}

        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            result[i] = 1 + result.get(i, 0)

        for key, v in result.items():
            freq[v].append(key)

        answer = []
        for i in range(len(freq) - 1, -1, -1):

            for j in freq[i]:

                answer.append(j)

                if len(answer) == k:
                    return answer

        return answer
