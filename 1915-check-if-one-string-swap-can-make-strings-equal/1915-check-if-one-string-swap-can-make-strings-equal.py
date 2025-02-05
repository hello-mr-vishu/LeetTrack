class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        m = len(s1)
        n = len(s2)

        mismatches = 0
        mismatch = []
        pos = 0
        while pos < m:
            if s1[pos] != s2[pos]:
                mismatch.append(s1[pos])
                mismatch.append(s2[pos])
                mismatches += 1
            pos += 1
        if len(mismatch) == 4:
            return mismatch[0] == mismatch[3] and mismatch[1] == mismatch[2]
        return False
