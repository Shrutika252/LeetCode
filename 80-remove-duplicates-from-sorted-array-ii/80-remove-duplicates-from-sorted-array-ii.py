from collections import Counter
class Solution(object):
    def removeDuplicates(self, nums):
        count=0
        for i in nums:
            count=nums.count(i)
            while count>2:
                nums.pop(nums.index(i))
                count=count-1
            count=0
        
                
        return len(nums)
        
        
                
        
        