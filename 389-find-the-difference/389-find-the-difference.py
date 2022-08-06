class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        while s:
            for i in s:
                if i in t:
                    t=t.replace(i,'',1)
                    
        
            return t
        
        return t