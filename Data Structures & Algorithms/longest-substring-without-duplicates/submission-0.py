class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_answer = 0
        left = 0
        answer = 0

        for  i in range(len(s)):
            while s[i]  in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[i])
            answer = i - left +1
        
            max_answer= max(max_answer,answer)
        return max_answer
