class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for sub_s in s:
            hashmap[sub_s] = hashmap.get(sub_s, 0) + 1
        for sub_t in t:
            if sub_t not in hashmap:
                return False
            hashmap[sub_t] -= 1
            if hashmap[sub_t] < 0:
                return False
        for el in hashmap:
            if hashmap[el] > 0:
                return False
        return True