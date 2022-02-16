#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
import re


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        s_stack=[]
        t_stack=[]

        for word in s:
            if word=='#':
                if s_stack:
                    s_stack.pop()
            else:
                s_stack.append(word)
        
        for word in t:
            if word=='#':
                if t_stack:
                    t_stack.pop()
            else:
                t_stack.append(word)

        return s_stack==t_stack
        
            

# @lc code=end
