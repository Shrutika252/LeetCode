class Solution:
    def jump(self, nums: List[int]) -> int:
        start,end=0,0
        count=0
        res=0
        if len(nums)==1:
            return 0
        else:
            while end<len(nums)-1:
                for i in range(start,end+1):

                    count=max(count,i+nums[i])
                    
                start=end+1
                end=count
                res=res+1

                    
                    
        return res