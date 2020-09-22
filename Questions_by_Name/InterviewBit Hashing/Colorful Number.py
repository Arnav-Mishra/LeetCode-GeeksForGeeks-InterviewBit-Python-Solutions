class Solution:
# @param A : integer
# @return an integer
    def colorful(self, A):
    #first find all subsebts
        A=list(str(A))
        if(len(A)>1):
            sublist = [[]] 
            for i in range(len(A) + 1): 
                for j in range(i + 1, len(A) + 1): 
                    sub = A[i:j] 
                    sublist.append(sub) 
    #find the products of all subset digits 
    #use set since set doesn't take duplicate values
            b=set()
            for i in sublist:
                p=1
                for j in i:
                    p=p*int(j)
                b.add(p)
            if(len(b)==len(sublist)):
                return 1
            return 0
        else:
            return 1
