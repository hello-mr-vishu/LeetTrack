from collections import defaultdict

class Solution:
    def nC2(self, n):
        return (n * (n - 1)) // 2

    def tupleSameProduct(self, nums):
        n = len(nums)
        freq = defaultdict(int) 

        for i in range(n - 1):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                freq[product] += 1

        count = 0
        for frequency in freq.values():
            count += 8 * self.nC2(frequency)

        return count