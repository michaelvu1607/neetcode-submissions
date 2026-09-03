class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, = 0, 0
        cur_max = 0
        res = set()

        for r in range(len(s)):
            while s[r] in res:
                res.remove(s[l])
                l += 1
            res.add(s[r])
            len_sub = r - l + 1
            cur_max = max(cur_max, len_sub)

        return cur_max