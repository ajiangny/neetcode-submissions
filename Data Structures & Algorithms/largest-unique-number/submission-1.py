class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts = Counter(nums)
        unique_nums = [num for num, count in counts.items() if count == 1]
        return max(unique_nums) if unique_nums else -1