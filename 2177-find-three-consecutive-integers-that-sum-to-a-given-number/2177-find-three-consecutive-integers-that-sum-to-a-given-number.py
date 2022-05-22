class Solution(object):
    def sumOfThree(self, num):
        list1=[]
        list2=[]
        x=int(num/3)
        list1.append(x-1)
        list1.append(x)
        list1.append(x+1)
        
        if sum(list1)==num:
            return sorted(list1)
        
        else:
            return list2
            
        
        
        
        
        