class Solution:
    
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
        m = len(num1)
        n = len(num2)
        def find(i,j,k):
            if i>=m:
                return num2[j+k-1]
            if j>=n:
                return num1[i+k-1]
                
            if k == 1:
                return min(num1[i],num2[j])
            
            p = k//2
            mid1 = min(i+p-1,m-1)
            mid2 = min(j+p-1,n-1)

            r1 = mid1 - i + 1
            r2 = mid2 - j + 1

            if(num1[mid1]<num2[mid2]):
                return find(mid1+1,j,k-r1)
            else:
               return find(i,mid2+1,k-r2)
        

        if (m+n)%2== 1:
            return find(0,0,(m+n)//2+1)
        else:
            return (find(0,0,(n+m)//2+1) + find(0,0,(n+m)//2))/2

        



 



        