# -*- coding:utf-8 -*-
#给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

#括号必须以正确的顺序关闭，"()" 和 "()[]{}" 是有效的但是 "(]" 和 "([)]" 不是。

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        dict={"]":"[","}":"{",")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():

                if stack==[] or dict[char]!=stack[-1]:
                    return False
                else:
                    del stack[-1]#如果想省略此步骤，可以直接用stack.pop()操作，既弹出栈顶，又删除原先的栈。
            else:
                return False
        if len(stack)!=0:
            return False
        return True

s=Solution()
print s.isValid('{}[]')

a=['123','456']
print a.pop()#注意做了pop操作之后原来的list也发生了改变
print a
