class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def b(i,sum,l):
            if sum == target:
                ans.append(l.copy())
                return
            if i == len(candidates):
                return
            
            for j in range(i,len(candidates)):
                temp = candidates[j]
                if j != i and candidates[j] == candidates[j-1]:
                    continue
                if sum+temp<=target:
                    l.append(temp)
                    b(j+1,sum+temp,l)
                    l.pop()
        b(0,0,[])
        return ans
