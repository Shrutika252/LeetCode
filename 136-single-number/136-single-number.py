class Solution(object):
    def singleNumber(self, nums):
        for i in range(len(nums)):
            sum=nums.count(nums[i])
            if sum==1:
                break
        return nums[i]        
           
        