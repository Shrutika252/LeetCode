class Solution:
    def reverseString(self, s: List[str]) -> None:
        temp=[]
        i=len(s)-1
        while i>=0:
            temp.append(s[i])
            i=i-1
            
        j=0
        for i in temp:
            s[j]=i
            j=j+1
            
        return s
            