#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
from inspect import stack
import re


class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={'(':')','{':'}','[':']'}

        for char in s:
            if char in pairs:
                stack.append(char)
            elif len(stack)==0 or pairs[stack.pop()]!=char:
                return False
        return len(stack)==0 
           

            

        
# @lc code=end

