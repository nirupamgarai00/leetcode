class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def b(i,s,l):
            if target-s == 0:
                ans.append(l.copy())
                return
            if i == len(candidates):
                return

            for t in range(i,len(candidates)):
                c =candidates[t] 
                if s+c<=target:
                    l.append(c)
                    b(t,s+c,l)
                    l.pop()
                

        b(0,0,[])
        return ans    
                


            
            


        