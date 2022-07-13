class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        res=[]
        res=nums1+nums2
        res.sort()
        
        if len(res)%2!=0:
            m1 = int(len(res)/2)
            median=float(res[m1])
            return median
           
        else:
            m1 = int(len(res)/2 - 1)
            m2 = int(len(res)/2)
            median=float(res[m1]+res[m2])/2
            return median
            


        