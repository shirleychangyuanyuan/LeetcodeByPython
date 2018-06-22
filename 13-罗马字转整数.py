# -*- coding:utf-8 -*-
#给定一个罗马数字，将其转换成整数。
#返回的结果要求在 1 到 3999 的范围内。
#罗马数字采用7个罗马字母作为数字。即I（1）、X（10）、C（100）、M（1000）、V（5）、L（50）、D（500）
#计数方法：
#相同的数连写，所表示的数表示这些数字相加得到的数，III=3
#大数--小数，表示这些数字相加得到的数，VIII=8,XII=12
#小数（I\X\C）--大数，表示大数减小数得到的数。
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        sum=0
        for i in range(0,len(s)-1):
            if roman[s[i]]< roman[s[i+1]]:#减去当前的数
                sum-=roman[s[i]]
            else:#包括了如果相邻两个相等，也是相加。加上当前的数
                sum+=roman[s[i]]
        return sum+roman[s[-1]]#别忘了加上最后一个数。
