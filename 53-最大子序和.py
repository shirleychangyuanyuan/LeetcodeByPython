# -*- coding:utf-8 -*-
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
        	return nums[0]
        g = l = -10000000
        for n in nums:
        	l = max(n, n + l)
        	g = max(l, g)
        return g
if __name__ == '__main__':
	print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
	

