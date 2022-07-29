class Solution:
    def hammingWeight(self, n: int) -> int:
        str_res=str(bin(n)).count('1')
        return str_res