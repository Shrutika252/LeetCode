class Solution(object):
    def removeElement(self, nums, val):
        i=0
        while i<len(nums):
            if val==nums[i]:
                nums.pop(i)
            else:
                i=i+1
        return len(nums)
        