class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        
        if len(nums)==0:
            return []
        
        if len(nums)==1:
            return [nums]
        
        res=[[num] + r 
			for i, num in enumerate(nums) 
            for r in self.permute(nums[:i] + nums[i+1:])]
        
        return res
        