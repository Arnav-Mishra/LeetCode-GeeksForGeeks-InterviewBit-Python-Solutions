class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        Listans = []
        A.sort()
        def permute(curSum,options,Set):
            if curSum==B:
                Listans.append(Set[:])
                return
            if curSum>B:
                return
            for i in range(len(options)):
                permute(curSum+options[i],options[i:],Set+[options[i]])
        
        permute(0,A,[])
        ans = []
        for i in Listans:
            if i not in ans:
                ans.append(i)
        return ans
