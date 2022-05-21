class Solution(object):
    def plusOne(self, digits):
        s=[str(i) for i in digits]
        nums=int(''.join(s))
        nums=int(nums)+1
        s1=str(nums)
        res=list(s1)
        return res