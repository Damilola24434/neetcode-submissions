class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        large = 0
        max_large = 0
        left = 0

        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left +=1
            seen.add(s[i])
            large = i-left +1
            max_large = max(max_large, large)
        return max_large
