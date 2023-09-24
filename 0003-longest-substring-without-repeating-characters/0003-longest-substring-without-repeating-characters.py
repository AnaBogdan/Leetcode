class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        rez = 0
        Myset = set()
        for r in range(len(s)):
            while s[r] in Myset:
                Myset.remove(s[l])
                l += 1
            Myset.add(s[r])
            rez = max(rez, r - l + 1)

        return rez