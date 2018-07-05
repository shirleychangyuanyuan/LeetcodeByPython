# -*- coding:utf-8 -*-
# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，
# 使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict = {}
        for i in range(len(nums)):
        	
        	if nums[i] in dict and i - dict[nums[i]] <= k:
        		return True
        	else:
        		dict[nums[i]] = i
        return False












if __name__ == '__main__':
	print(Solution().containsNearbyDuplicate([1,2,3,1], k =3))
	print(Solution().containsNearbyDuplicate([1,2,3,1,2,3], k =2))
	print(Solution().containsNearbyDuplicate([1,0,1,1], k = 1))

        