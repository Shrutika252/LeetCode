class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        ans=[]
        
        
        def recurseparen(start,end):
            if start==end==n:
                ans.append("".join(stack))
                return
            
            if start<n:
                stack.append("(")
                recurseparen(start+1,end)
                stack.pop()
                
                
            if end<start:
                stack.append(")")
                recurseparen(start,end+1)
                stack.pop()
                
        recurseparen(0,0)  
        return ans
            
            
        
                