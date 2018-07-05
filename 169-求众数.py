# -*- coding:utf-8 -*-
# 给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

# 你可以假设数组是非空的，并且给定的数组总是存在众数。
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for key in nums:
        	dict[key] = dict.get(key,0) + 1
        	if dict[key] > len(nums)/2:
        		return key
# nums = [2,4,6,7,7,9,8]
# dict = {}
# for key in nums:
# 	dict[key] = dict.get(key,0) +1
# print(dict)
