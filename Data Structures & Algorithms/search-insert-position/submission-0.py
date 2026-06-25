class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        lowestIndex = 0

        for i in range(len(nums)):
            if target == nums[i]:
                return i

            if target > nums[i]:
                lowestIndex = i

        if target < nums[lowestIndex]:
            return lowestIndex
        else:
            return lowestIndex + 1

        