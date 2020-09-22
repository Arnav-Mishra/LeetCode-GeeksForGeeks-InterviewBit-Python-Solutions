class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        if len(A)==0:
            return [[]]
        return [[A[i]]+x for i in range(len(A)) for x in self.permute(A[:i]+A[i+1:])]
