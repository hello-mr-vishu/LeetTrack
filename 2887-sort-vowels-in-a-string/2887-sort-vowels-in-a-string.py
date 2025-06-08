class Solution:
    def sortVowels(self, s: str) -> str:
        # lst=[]
        # for i in range(len(s)):
        #     lst.append(ord(s[i]))
        # print(lst)
        # print(111-97)
        # hm = {}
        # vowels = ['A','E','I','O','U','a','e','i','o','u']
        # for i in range(len(s)):
        #     hm[ord(vowels[i])] = vowels[i]
        vow = []
        pos = []

        for i , ch in enumerate(s):
            if ch.lower() in {'a','e','i','o','u'}:
                vow.append(ch)
                pos.append(i)
        print(vow)
        vow.sort()
        print(vow)
        ans = list(s)
        for i , v in zip(pos,vow):
            ans[i]=v
        return ''.join(ans)