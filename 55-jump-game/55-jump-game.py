class Solution(object):
    def canJump(self, nums):
        count=0
        for i in range(len(nums)):
            if i>count:
                return False
            else:
                count=max(count,i+nums[i])
        return True