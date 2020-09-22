class Solution:
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        Dict = {'0':'0','1':'1','2':'abc','3':'def','4':'ghi','5':'jkl',
        '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        def ret(arr):
            if len(arr)<1:
                return []
            if len(arr)==1:
                return list(Dict[arr[0]])
            else:
                M = [x+i for x in Dict[arr[0]] for i in ret(arr[1:])]
            return sorted(M)
        
        ans = ret(A)
        return ans
