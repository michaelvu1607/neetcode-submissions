class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest_streak = 0

        for n in set_nums:
            if (n-1) not in set_nums:
                current_num = n
                current_streak = 1
                while (current_num+1) in set_nums:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(current_streak, longest_streak)

        return longest_streak
