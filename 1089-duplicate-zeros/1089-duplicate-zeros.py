class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n=len(arr)
        if all([x!=0 for x in arr]):
            return arr
        else:
            stack=[]
            for i in range(n):
                stack.append(arr[i])
                if arr[i]==0:
                    stack.append(0)
            for j in range(n):
                arr[j]=stack[j]
                
        return arr
       
            