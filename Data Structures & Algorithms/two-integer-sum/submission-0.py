class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}
        for idx,num in enumerate(nums):
            diff = target - num 
            if diff in sum_dict:
                return [sum_dict[diff],idx]
            sum_dict[num] = idx
        

        