class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         initial_length = len(nums)
         final_length = len(set(nums))

         return initial_length != final_length
