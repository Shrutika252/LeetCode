class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res=[]
        last_index=0
        if target in nums:
            first_index=nums.index(target)
            
            
            for i in range(len(nums)):
                if nums[i]==target:
                    last_index=i
                    
            res.append(first_index)
            res.append(last_index)
            
            return res
        
        else:
            return [-1,-1]


       
    
        
        
        
        