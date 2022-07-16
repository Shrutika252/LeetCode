class Solution(object):
    def climbStairs(self, n):
        flag=0
        count=1
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            x, y = 1, 1
            for _ in range(n):
                x,y=y, x+y
               
            return x
                
            
            
            
            