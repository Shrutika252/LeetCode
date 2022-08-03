class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        list1=[num1,num2]
        res=[]
        num=0
        
        for i in range(len(list1)):
            s=list1[i]
            
            for j in s:
                num = num * 10 + (ord(j) - 48) 
                
            res.append(num)
            num=0
            
        mul=1
        for i in res:
            mul=mul*i

        return str(mul)
        
        