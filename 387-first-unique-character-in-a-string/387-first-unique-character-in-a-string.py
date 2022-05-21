class Solution(object):
    def firstUniqChar(self, s):
        for i in s:
            sum=s.count(i)
            if sum==2:
                continue
            if sum==1:
                break
        if sum==1:
            return s.index(i)
        else:
            return -1