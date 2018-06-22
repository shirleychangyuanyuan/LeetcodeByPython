# -*- coding:utf-8 -*-
#给定一个整数数列，找出其中和为特定值的那两个数。
#你可以假设每个输入都只会有一种答案，同样的元素不能被重用。
#给定 nums = [2, 7, 11, 15], target = 9
#因为 nums[0] + nums[1] = 2 + 7 = 9
#所以返回 [0, 1]
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length=len(nums)
        for i in range(length):
            if target-nums[i] in nums[i+1:]:#在或者不在。成员关系操作符in not in
                return [i,nums.index(target-nums[i],i+1)]#注意索引不包括i本身。限制范围
# arr=[1,2,3,4]
# print(arr.index(4))
s=Solution()

print s.twoSum([3,3],6)