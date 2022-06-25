class Solution(object):
    def searchRange(self, nums, target):
        res=[]

        if target in nums:
            res.append(nums.index(target))
        
            nums.reverse()
            temp = nums.index(target)
            index=(len(nums) - temp - 1)
            res.append(index)
            
        else:
            res.append(-1)
            res.append(-1)
            
        return res
