class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        slow = 0
        fast = 1
        res = []
        while slow < len(s):
            while s[fast] != '#':
                fast += 1
            len_s = int(s[slow:fast])
            slow = fast + 1
            fast = slow + len_s
            res.append(s[slow:fast])
            slow = fast
            fast += 1
        return res
