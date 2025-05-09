class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # minlen = min(len(word1),len(word2))
        # s=""
        # for i in range(minlen):
        #     s+=word1[i]
        #     s+=word2[i]
        # s+= word1[minlen:] + word2[minlen:]
        # return s
        res = []
        i = 0
        while i<len(word1) or i<len(word2):
            if i<len(word1):
                res.append(word1[i])
            if i<len(word2):
                res.append(word2[i])
            i+=1
        return ''.join(res)