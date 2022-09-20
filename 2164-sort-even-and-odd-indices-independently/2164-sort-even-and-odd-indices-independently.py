class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even=[]
        odd=[]
        n=len(nums)
        for i in range(len(nums)):
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
                
        even.sort()
        odd.sort(reverse=True)
        
        x=0
        y=0
        nums=[]
        for i in range(n):
            if i%2==0:
                nums.append(even[x])
                x+=1
                
            else:
                nums.append(odd[y])
                y+=1
                
        return nums
            