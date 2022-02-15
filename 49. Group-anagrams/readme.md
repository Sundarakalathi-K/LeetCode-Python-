# Group Anagrams
Category | Difficulty |	Likes |	Dislikes
algorithms |	Medium | (63.34%)	| 8252 |	285
Tags
Companies
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.


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
    
       
        



