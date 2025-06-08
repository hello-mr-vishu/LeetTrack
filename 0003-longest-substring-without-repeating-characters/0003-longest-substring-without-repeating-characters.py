class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # seen = set()
        m = 0
        for i in range(len(s)):
            seen = set()
            cnt = 0
            for j in range(i,len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
                cnt += 1
            m = max(m,cnt)
        return m