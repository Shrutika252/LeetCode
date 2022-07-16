class Solution(object):
    def minMoves2(self, nums):
        nums.sort()
        ans=0
        res=0
        mid=len(nums)/2
        
        hold=nums[mid]
        
        for i in range(len(nums)):
            ans=abs(nums[i]-hold)
            res=res+ans
            
        return res
        
        
        
        