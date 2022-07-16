class Solution(object):
    from collections import Counter
    def isAnagram(self, s, t):
        if Counter(s)==Counter(t):
            return True
        else:
            return False
        
       
                
        
        