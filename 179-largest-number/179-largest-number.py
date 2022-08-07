class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res=''

        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                x,y=str(nums[i]),str(nums[j])
                if y+x>x+y:
                    nums[j],nums[i]=nums[i],nums[j]
                    
        for j in nums:
            res=res+str(j)

        if res[0]=='0':
            return '0'
        else:
            return res