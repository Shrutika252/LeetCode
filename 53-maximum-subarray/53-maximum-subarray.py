class Solution(object):
    def maxSubArray(self, nums):
        if len(nums)==1:
            return nums[0]
        else:
            maxnum=nums[0]
            curnum=nums[0]
            
            for i in range(1,len(nums)):
               
                curnum=max(nums[i],curnum+nums[i])
                maxnum=max(maxnum,curnum)
            
            return maxnum
                
        
        