class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes, counter = 0, 0

        for num in nums:
            if num == 1:
                counter += 1
                maxOnes = max(maxOnes, counter)
            else:
                counter = 0
        
        return maxOnes