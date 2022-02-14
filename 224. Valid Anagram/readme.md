Valid Anagram
Category	Difficulty	Likes	Dislikes
algorithms	Easy (60.94%)	4179	199
Tags
Companies
amazon | uber | yelp

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

Solution:


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        char_count={}
        
        for i in s:
            if i not in char_count:
                char_count[i]=1
            else:
                char_count[i]+=1
        
        for i in t:
            if i not in char_count or char_count[i]==0:
                return False
            else:
                char_count[i]-=1
        return True
    
        
# @lc code=end

