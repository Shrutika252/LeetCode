class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ans=s[1:]+s[:-1]
        
        return s in ans
        
       