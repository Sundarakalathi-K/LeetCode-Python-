#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
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

