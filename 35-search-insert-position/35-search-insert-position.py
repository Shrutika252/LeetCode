class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        elif target not in nums:
            nums.append(target)
            nums.sort()
            return nums.index(target)
               
                 

       