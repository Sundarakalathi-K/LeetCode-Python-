# 20. Valid Parentheses 
Category	| Difficulty | 	Likes | Dislikes <br><br>
algorithms	| Easy | (40.61%)	| 11239	| 476 <br><br>
Tags :
string | stack <br><br>

Companies ::
airbnb | amazon | bloomberg | facebook | google | microsoft | twitter | zenefits <br>

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. <br>

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.


solution:

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
           

         


