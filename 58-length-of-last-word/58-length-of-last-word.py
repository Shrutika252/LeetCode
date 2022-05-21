class Solution(object):
    def lengthOfLastWord(self, s):
        strs=s.split()
        res=strs[-1]
        length=len(res)
        return length