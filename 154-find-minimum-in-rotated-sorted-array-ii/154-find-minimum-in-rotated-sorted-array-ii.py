class Solution(object):
    def findMin(self, nums):
        nums.sort()
        res=set(nums)
        return min(res)
        