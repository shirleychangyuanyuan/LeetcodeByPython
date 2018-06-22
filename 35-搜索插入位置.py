# -*- coding:utf-8 -*-
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

# 你可以假设数组中无重复元素。
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
        	return nums.index(target)
        else:
        	for i in range(len(nums)):
        		if nums[i] > target :
        			return i
        		
        return len(nums)

if __name__ == '__main__':
	print(Solution().searchInsert([1,3,5,6],0))
