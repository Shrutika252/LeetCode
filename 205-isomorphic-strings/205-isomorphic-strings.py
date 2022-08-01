class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        
        dict1={}
        temp=set()
        for i in range(len(s)):
            x=s[i]
            y=t[i]
            
            
            if x in dict1:
                
                if dict1[x]!=y:
                    return False
                
            else:
                
                
                if y in temp:
                    return False
                
                
                dict1[x]=y
                temp.add(y)
          
        return True
                    
            
            