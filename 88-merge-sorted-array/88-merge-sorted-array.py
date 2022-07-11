class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for i in nums2:
            nums1.append(i)
            nums1.remove(0)
        nums1.sort()

        return nums1
        
        
        
    