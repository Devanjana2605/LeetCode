
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:
            return 0
        sum=0
        newstr=" "
        for i in str(n):
            if int(i)!=0:
                newstr=newstr+i
                sum=sum+int(i)



        
        newstr=sum*int(newstr)
        return newstr      

