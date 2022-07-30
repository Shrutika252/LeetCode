class Solution:
    def reverseWords(self, s: str) -> str:
        temp=s.split()
        temp.reverse()
        final=(' '.join(temp))
        
        
        return final
       