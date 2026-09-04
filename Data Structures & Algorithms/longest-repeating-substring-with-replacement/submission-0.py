class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letter_count = {}
        cur_max = 0
        l = 0

        for r in range(len(s)):
            letter_count[s[r]] = letter_count.get(s[r], 0) + 1

            while (r - l + 1) - max(letter_count.values()) > k:
                letter_count[s[l]] -= 1
                l += 1
                
            window_len = r - l + 1
            cur_max = max(cur_max, window_len)

        return cur_max
            