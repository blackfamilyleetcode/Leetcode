# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.


class Solution:
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        _ = {}
        for i in range(len(nums)):
            if nums[i] in _:
                return [_[nums[i]], i]
            else:
                _[target - nums[i]] = i

# Runtime: 40 ms, faster than 77.95% of Python3 online submissions for Two Sum.
# Memory Usage: 14.6 MB, less than 19.31% of Python3 online submissions for Two Sum.
