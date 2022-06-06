class Solution(object):
    def longestPalindrome(self, s):
        substr= ''
        
        for i in range(len(s)):
            j=k=i
            while j>=0 and k<len(s) and s[j]==s[k]:
                j=j-1
                k=k+1
            prev=s[j + 1:k]
            j=i
            k=i+1
            while j>=0 and k<len(s) and s[j]==s[k]:
                j=j-1
                k=k+1
            curr=s[j + 1:k]
            
            substr= max(prev,curr,substr,key=len)
        return substr