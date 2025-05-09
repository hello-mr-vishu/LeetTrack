class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minlen = min(len(word1),len(word2))
        s=""
        for i in range(minlen):
            s+=word1[i]
            s+=word2[i]
        s+= word1[minlen:] + word2[minlen:]
        return s