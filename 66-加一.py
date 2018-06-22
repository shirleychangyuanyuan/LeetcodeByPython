# -*- coding:utf-8 -*-
import math
# 给定一个非负整数组成的非空数组，在该数的基础上加一，返回一个新的数组。

# 最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

# 你可以假设除了整数 0 之外，这个整数不会以零开头。
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        # list = [i for i in range(len(digits))]
        # list.reverse()
        # sum = 0
        # for i in range(len(digits)):
        # 	sum = sum + digits[i] * 10**list[i]
        # sum = int(sum)
        # new_sum = str(sum + 1)
        # final_sum = [int(new_sum[i]) for i in range(len(new_sum))]
        # return final_sum
        carry = 1
        for i in range(len(digits)-1,-1,-1):
        	total = digits[i] + carry
        	digit = int(total % 10)
        	carry = int(total / 10)
        	digits[i] = digit
        if carry ==1:
        	digits.insert(0,1)
        return digits
if __name__ == '__main__':
	print(Solution().plusOne([6,1,4,5,3,9,0,1,9,5,1,8,6]))
	