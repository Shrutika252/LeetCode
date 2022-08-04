class Solution:
    def reverseVowels(self, s: str) -> str:
        stack=[]
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        for i in s:
            if i in vowels:
                stack.append(i)
            
            
        temp=list(s)
        for j in range(len(temp)):
            if temp[j] in vowels:
                temp[j]=stack[-1]
                stack.pop()
                
        res=''
        for i in temp:
            res=res+i
        return res

        
            