class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = {}
        arr = []
        for num in nums:
            if num in elements:
                elements[num] += 1
            else:
                elements[num] = 1

        sorted_elements = sorted(elements.items(), key=lambda item: item[1], reverse=True)

        return [li[0] for li in sorted_elements[:k]]
            

