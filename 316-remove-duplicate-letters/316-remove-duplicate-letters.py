from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        res=''
        latest_index={}
        stack=[]
        visited=set()
        
        
        for i in range(len(s)):
             latest_index[s[i]]=i
                
                
        
            
        for i in range(len(s)):
            if s[i] not in visited:
                while stack and stack[-1]>s[i] and latest_index[stack[-1]]>i:
                    visited.remove(stack.pop())

                stack.append(s[i])
                visited.add(s[i])
                
          
        res=''.join(stack)
        return res
                
        
                
        
        