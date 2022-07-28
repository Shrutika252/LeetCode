class Solution:
    def isPalindrome(self, s: str) -> bool:
        final=''
        for ch in s:
            if ch.isalnum():
                final=final+ch
        print(final)
        res=final.lower()
        print(res)
        print(res[::-1])
        if res==res[::-1]:
            return True
        else:
            return False
        