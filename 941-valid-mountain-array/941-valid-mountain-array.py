class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        incline=False
        decline=False
        if len(arr)<3:
            return False
        else:
            for i in range(len(arr)-1):
                if arr[i]<arr[i+1] and not decline:
                    incline=True
                    
                elif arr[i]>arr[i+1] and incline:
                    decline=True
                    
                else:
                    return False
                
            
            if incline and decline:
                return True
            return False