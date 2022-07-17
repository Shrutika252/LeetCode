import math
class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        final=[]
        
        if p1==0 and p2==0 and p3==0 and p4==0:
            return False
        def distance(x,y):
            return math.sqrt((y[0] - x[0])**2 + (y[1] - x[1])**2)
        
        
        d1=distance(p1,p2)
        d2=distance(p2,p3)
        d3=distance(p3,p4)
        d4=distance(p1,p4)
        d5=distance(p1,p3)
        d6=distance(p2,p4)
        
        final.append(d1)
        final.append(d2)
        final.append(d3)
        final.append(d4)
        final.append(d5)
        final.append(d6)
           
        final.sort()
        if final[0]==final[1]==final[2]==final[3] and final[4]==final[5]==0:
            return False
        elif final[0]==final[1]==final[2]==final[3] and final[4]==final[5]:
            return True
        else:
            return False


