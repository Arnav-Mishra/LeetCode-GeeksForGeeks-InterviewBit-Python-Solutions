class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        options = ['0','1']
        List = []
        
        def combinations(n):
            if n==1:
                return ['0','1']
            else:
                return ['0'+i for i in combinations(n-1)]+['1'+i for i in combinations(n-1)[::-1]]
        return [int(i,2) for i in combinations(A)]
