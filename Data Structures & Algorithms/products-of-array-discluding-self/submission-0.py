class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        output = []

        for i in range(len(nums)):
            if i == 0:
                prefix = 1
                suffix = math.prod(nums[i+1:len(nums)])
                output.append(prefix * suffix)
            elif i == len(nums) - 1:
                prefix = math.prod(nums[0:i])
                suffix = 1
                output.append(prefix * suffix)
            else:
                prefix = math.prod(nums[0:i])
                suffix = math.prod(nums[i+1:len(nums)])
                output.append(prefix * suffix)

        return output