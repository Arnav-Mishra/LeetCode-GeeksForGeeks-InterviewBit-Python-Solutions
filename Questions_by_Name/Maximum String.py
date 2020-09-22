class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def solve(self, A, B):
        def swap(string,i,j):
            s1=string[:i]
            s2=string[i+1:j]
            s3=string[j+1:]
            return s1+string[j]+s2+string[i]+s3
        def sswap(A,B,ans):
            if B==0:
                return ans[0]
            for i in range(len(A)):
                for j in range(i+1,len(A)):
                    if A[j]>A[i]:
                        temp=swap(A,i,j)
                        if ans[0]<temp:
                            ans[0]=temp
                        sswap(temp,B-1,ans)
                        
        ans=[A]
        sswap(A,B,ans)
        return ans[0]
