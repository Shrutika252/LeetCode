from collections import Counter
class Solution(object):
    def removeDuplicates(self, nums):
        i=0
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                nums.pop(i+1)
            else:
                i=i+1
        return len(nums)
        