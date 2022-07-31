from collections import Counter
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        res={}
        for i,x in enumerate(nums):
            if x in res:
                if abs(i-res[x])<=k:
                    return True
        
            res[x]=i
                
        return False
        
        
        
        
        