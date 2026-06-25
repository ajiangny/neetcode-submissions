class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pos = 1

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            elif nums[i] != nums[i + 1]:
                nums[pos] = nums[i+1]
                pos += 1

        return pos
