#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # O(n)

        max_reach=0
        for curr_step in range(len(nums)):
            if curr_step>max_reach:
                return False
            curr_reach=curr_step+nums[curr_step]
            max_reach=max(curr_reach,max_reach)
        return True
        
# @lc code=end

