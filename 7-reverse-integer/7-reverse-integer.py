class Solution(object):
    def reverse(self, x):
        if x<0:
            temp=abs(x)
            temp1=str(temp)
            temp2=int(temp1[::-1])
            res=-temp2
        
        else:
            temp=str(x)
            res=int(temp[::-1])
        
        if abs(res) < 2**31 and res != 2**31 - 1:
            return res
        else:
            return 0
        
        