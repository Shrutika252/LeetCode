class Solution:
    def smallestNumber(self, num: int) -> int:
        temp=str(num)
        hold=[]
        count=0
        res=''
        
        
        if num==0:
            return num
        
        elif num>0:
            hold=list(temp)
            hold.sort()
            
            for i in range(len(hold)):
                if int(hold[i]) > 0 and hold[0] == '0':
                    hold[0] = hold[i]
                    hold[i] = '0'
                    break
            
            
            print(hold)
            for j in hold:
                res=res+j
                
            return int("".join(res))
                
                    

            
            
        elif num<0:
            for i in temp:
                if i!= '-':
                    hold.append(int(i))
            hold.sort(reverse=True)
            
            for i in hold:
                res=res+str(i)
                
            return -1* int("".join(res))
        