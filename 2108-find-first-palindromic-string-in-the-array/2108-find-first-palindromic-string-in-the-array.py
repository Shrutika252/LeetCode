class Solution(object):
    def firstPalindrome(self, words):
        n=len(words)
        for i in range(0,n): 
            rev=words[i][::-1]
            if words[i]==rev:
                return words[i]
        return ""
        