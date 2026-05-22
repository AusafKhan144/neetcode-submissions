class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
    
        solution = set()

        for cIdx in range(0, len(nums) - 2):
            leftIdx = cIdx + 1
            rightIdx = len(nums)-1

            while leftIdx < rightIdx:
                sum = nums[cIdx] + nums[leftIdx] + nums[rightIdx]  

                if sum == 0: 
                    triplets = (nums[cIdx], nums[leftIdx], nums[rightIdx])
                    solution.add(triplets)
                if sum > 0: 
                    rightIdx -= 1
                else: 
                    leftIdx += 1
                 
        return list(solution)
