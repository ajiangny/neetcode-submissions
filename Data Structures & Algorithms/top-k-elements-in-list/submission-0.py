class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_mapping = {}

        for i in nums:
            if i not in nums_mapping:
                nums_mapping[i] = 0

            nums_mapping[i] += 1

        result = sorted(nums_mapping, key=nums_mapping.get, reverse=True)
        
        return result[:k]
        

