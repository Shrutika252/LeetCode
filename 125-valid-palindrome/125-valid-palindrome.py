class Solution(object):
    def isPalindrome(self, s):
        y=s.lower()
        y=''.join (ch for ch in y if ch.isalnum())
        if y == y[::-1]:
            return True
        else:
            return False