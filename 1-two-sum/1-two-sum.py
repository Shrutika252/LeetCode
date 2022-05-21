class Solution(object):
    def twoSum(self, nums, target):
        list1=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    list1.append(i)
                    list1.append(j)
                    break
        return list1
        
        