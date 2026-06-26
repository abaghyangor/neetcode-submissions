class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}

        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        sorted_vals = dict(sorted(freqs.items(), key=lambda x: x[1], reverse=True))
       
        return list(sorted_vals.keys())[:k]