class Solution(object):
    def minMoves(self, nums):
        nums.sort()
        res=0
        
        if all(i==nums[0] for i in nums):
            return 0
        
        for i in range(1,len(nums)):
            ans=nums[i]-nums[0]
            res=res+ans
        
            
        
        return res
        
        