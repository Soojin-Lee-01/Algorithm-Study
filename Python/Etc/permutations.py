class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def permutation(n, combo = []):
            if len(combo) == len(nums):
                answer.append(combo[:])
                return

            for i in range(len(nums)):
                if nums[i] not in combo:
                    combo.append(nums[i])
                    permutation(n, combo)
                    combo.pop()

        permutation(len(nums))


        return answer
        
