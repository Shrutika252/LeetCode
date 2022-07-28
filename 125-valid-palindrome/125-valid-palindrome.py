class Solution:
    def isPalindrome(self, s: str) -> bool:
        final=''
        for ch in s:
            if ch.isalnum():
                final=final+ch

        res=final.lower()
        if res==res[::-1]:
            return True
        else:
            return False
        