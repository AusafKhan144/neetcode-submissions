class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0
        for num in nums:
            previous_num = num - 1 
            current_length = 1
            if previous_num not in nums_set:
                while num + current_length in nums_set:
                    current_length += 1
            max_length = max(current_length,max_length)
        return max_length
