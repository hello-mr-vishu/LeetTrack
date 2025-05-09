class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        maxres = 0
        for i in range(len(s)):
            char_set = set()
            res = 0
            for j in range(i,len(s)):
                if s[j] in char_set:
                    break
                char_set.add(s[j])
                res+=1
            maxres= max(res,maxres)
            print(char_set)            
        return maxres