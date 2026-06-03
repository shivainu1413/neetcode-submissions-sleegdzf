class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
        return [el[0] for el in sorted(hashmap.items(), key=lambda x: x[1], reverse=True)[:k]]
                