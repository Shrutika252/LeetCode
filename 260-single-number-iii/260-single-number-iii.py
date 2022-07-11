class Solution(object):
    def singleNumber(self, nums):
        res=[]
        i=0
        while i<len(nums):
            val=nums.count(nums[i])
            if val==1:
                res.append(nums[i])
            i=i+1
        return res
            
        