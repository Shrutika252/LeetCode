from collections import Counter
class Solution(object):
    def containsDuplicate(self, nums):
        dict1={}
        dict1=Counter(nums)
        for i in dict1.values():
            if i>=2:
                return True
            
        return False