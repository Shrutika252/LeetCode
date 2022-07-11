class Solution(object):
    def singleNumber(self, nums):
        for i in range(len(nums)):
            val=nums.count(nums[i])
            if val==1:
                return nums[i]
        