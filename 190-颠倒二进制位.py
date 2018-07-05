# -*- coding:utf-8 -*-
# 颠倒给定的 32 位无符号整数的二进制位。
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
    	b = bin(n)[2:][::-1]
    	return int(b + '0'*(32-len(b)),2)


print(bin(43261596))
print(bin(43261596)+'0'*2)