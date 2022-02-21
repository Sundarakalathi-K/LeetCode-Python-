#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
import re


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp_sequence=[1]*len(nums)
        max_range_length=0

        for j in range(1,len(nums)):
            for i in range(j):
                if nums[i]<nums[j]:
                    dp_sequence[j]=max(dp_sequence[i]+1,dp_sequence[j])
            max_range_length=max(max_range_length,dp_sequence[j])
        # return max_range_length
        return max(dp_sequence)




        
# @lc code=end

