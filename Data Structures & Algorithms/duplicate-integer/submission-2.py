class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        nums_set = list(nums_set)
        if len(nums) <= len(nums_set):
            return False
        else:
            return True