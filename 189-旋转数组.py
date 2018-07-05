# -*- coding:utf-8 -*-
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 要求使用空间复杂度为 O(1) 的原地算法。

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        self.reversePart(nums,0,len(nums)-k-1)
        self.reversePart(nums,len(nums)-k,len(nums)-1)
        self.reversePart(nums,0,len(nums)-1)
        return nums
    def reversePart(self,nums,start,end):
    	while start < end:
    		nums[start],nums[end] = nums[end],nums[start]
    		start, end = start + 1, end -1
#         # k = k % len(nums)
#         # nums[:k], nums[k:] = nums[len(nums)-k:], nums[:len(nums)-k]

#         # old_nums = [:]
#         # for i in range(len(nums)):
#         # 	nums[(i+k) %len(nums)] = old_nums[i]

if __name__ == '__main__':
	print(Solution().rotate([1,2,3,4,5,6,7],3))