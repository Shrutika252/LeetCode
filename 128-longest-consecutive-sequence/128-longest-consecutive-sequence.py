class Solution(object):
    def longestConsecutive(self, nums):
        x=sorted(nums)
        count=1
        temp=1
        
        if len(x)==1:
            return 1
        
        if len(x)==0:
            return 0
        
        for i in range(1,len(x)):
            if x[i-1]==x[i]:
                continue
                
            if x[i-1] +1 ==x[i]:
                temp=temp+1
            else:
                temp=1
            
            
            if temp>count:
                count=temp
                
        return count
            
        
                        
                        
                        
                    
                
                    

                
                    

                    
    
        
                    
                    
       