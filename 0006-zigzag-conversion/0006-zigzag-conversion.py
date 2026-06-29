class Solution:
    def convert(self, s: str, n: int) -> str:

        if n==1:
            return s
        ans = ''
        
        cycles = 2*(n-1)
        for i in range(n,0,-1):
            skip = 2*(i-1)
            k = n-i
            while(k<len(s)):
                ans += s[k]
                if cycles-skip != 0 and skip != 0 and k+skip<len(s):
                    ans += s[k+skip]
                k += cycles
            
        

        return ans
             







        