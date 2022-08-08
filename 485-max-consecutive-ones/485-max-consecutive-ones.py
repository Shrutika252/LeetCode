class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi=0
        count=0
        
        i=0
        while i<len(nums):
            if nums[i]==1:
                count=count+1
                maxi=max(maxi,count)
            elif nums[i]!=1:
                count=0
            i=i+1
                       
        return maxi