class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)

        i=0
        while i<=n+1:
            if i not in nums:
                return i
            i=i+1
            