# -*- coding:utf-8 -*-

# 给定一个整数数组，判断是否存在重复元素。

# 如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict = {}
        for key in nums:
        	dict[key] = dict.get(key,0) + 1
        	if dict[key] >= 2:
        		return True
        return False

if __name__ == '__main__':
	print(Solution().containsDuplicate([1,2,3,1]))
	print(Solution().containsDuplicate([1,1,1,3,3,2,3,4]))