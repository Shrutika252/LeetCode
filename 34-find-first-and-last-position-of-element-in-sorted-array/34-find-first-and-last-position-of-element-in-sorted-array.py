class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res=[]
        first_index=0
        last_index=0
        if target in nums:
            for i in range(len(nums)):
                if nums[i]==target:
                    first_index=i
                    break
                    
            
            
            for i in range(len(nums)):
                if nums[i]==target:
                    last_index=i
                    
            res.append(first_index)
            res.append(last_index)
            
            return res
        
        else:
            return [-1,-1]


       
    
        
        
        
        