# -*- coding:utf-8 -*-
# 给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums)
        for i in range(res):
        	res ^= nums[i] ^ i
        return res
if __name__ == '__main__':
	print(Solution().missingNumber(nums=[3,0,1]))