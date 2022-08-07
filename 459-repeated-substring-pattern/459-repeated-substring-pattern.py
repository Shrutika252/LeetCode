class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        ans=''
        for i in s:
            ans=ans+i
            if s.count(ans)*len(ans)==len(s) and len(ans)!=len(s):
                return True
        
        return False
        
        
       