
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        res=[i for i in nums if i%2==0]
        if len(res)==0:
            return -1
        else:
            ans=max(sorted(res),key=res.count)
            return ans