from collections import Counter
class Solution(object):
   
    def majorityElement(self, nums):
        dict1={}
        dict1=Counter(nums)
        major=max(dict1,key=dict1.get)
        return major
        
        
        