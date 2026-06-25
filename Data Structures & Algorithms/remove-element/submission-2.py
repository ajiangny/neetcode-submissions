class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        r = len(nums) - 1

        for i in range(len(nums)):
            while nums[r] == val and r > i:
                r -= 1

            if nums[i] == val and i < r:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            
            if nums[i] != val:
                count += 1


        return count
