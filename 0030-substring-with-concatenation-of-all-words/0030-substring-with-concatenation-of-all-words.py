class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        constraint = {}
        
        for i in words:
            if i not in constraint:
                constraint[i] = 1
                
            else:
                constraint[i] += 1
        ans = []
        
        k = len(words[0])
        for i in range(k):
            n = i
            m = i
            window = {}
            for j in range(i,len(s),k):
                word = s[j:j+k]
                if m-n == len(words)*k:
                    ans.append(n)

                if word in constraint:
                    if word not in window:
                        window[word] = 1
                        m += k
                    elif constraint[word]>window[word]:
                        window[word] += 1
                        m += k
                    else:
                        while constraint[word]<window[word]+1:
                            t = s[n:n+k]
                            window[t] -= 1
                            if window[t] == 0:
                                del window[t]
                            n += k
                            if word not in window:
                                break
                            
                             
                            
                        window[word] = 1 if word not in window else window[word] + 1
                        m += k
                else:
                    window = {}
                    n = j+k
                    m = j+k
            if m-n == len(words)*k:
                ans.append(n)
        
        return ans
                

                
                        

        