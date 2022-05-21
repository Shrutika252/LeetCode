class Solution(object):
    def strStr(self, haystack, needle):
        
        
       
        if needle in haystack:    
            hold=haystack.index(needle)
            return hold
        else:
            return -1
            