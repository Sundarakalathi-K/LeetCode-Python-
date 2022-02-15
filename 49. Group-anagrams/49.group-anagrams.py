#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from optparse import Values


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        grouping_words={}

        for words in strs:
            key="".join(sorted(words))
            print(key)

            if key in grouping_words:
                grouping_words[key].append(words)
            else:
                grouping_words[key]=[words]

        return reversed(list(grouping_words.values()))
    
       
        
# @lc code=end

