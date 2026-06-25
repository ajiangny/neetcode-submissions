class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """
        we can use a dict to check for seen ints
        subtract target with array until we find seen
        """
        
        seen = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in seen:
                return [seen[difference], i]
            
            seen[nums[i]] = i

        return []
