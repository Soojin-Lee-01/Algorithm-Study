class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates.sort()
        def dfs(t, combo = []):
            if sum(combo) == target:
                if combo not in answer:
                    answer.append(combo[:])
                    return
                
            for i in range(t, len(candidates)):
                if i > t and candidates[i] == candidates[i - 1]:
                    continue
                if sum(combo) + candidates[i] <= target:
                    combo.append(candidates[i])
                    dfs(i+1, combo)
                    combo.pop()
        dfs(0)

        return answer
