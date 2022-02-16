# Backspace String Compare <br>
Category | 	Difficulty |	Likes |	Dislikes<br><br>
algorithms	| Easy | (47.39%)	| 3558	| 166<br><br>

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
 
Solution::

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
        
            





