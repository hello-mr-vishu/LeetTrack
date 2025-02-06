from typing import List
from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        def nc2(n: int) -> int:
            return (n * (n - 1)) // 2  

        ht = defaultdict(int)  
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                ht[nums[i] * nums[j]] += 1  

        cnt = 0
        for key, values in ht.items():  
            if values >= 2:
                cnt += 8 * nc2(values)

        return cnt