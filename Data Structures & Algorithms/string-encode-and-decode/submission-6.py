class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        slow, fast = 0, 1
        res = []
        while slow < len(s):
            while s[fast] != "#" and fast < len(s):
                fast += 1
            len_str = int(s[slow:fast])
            slow = fast + 1
            fast = slow + len_str
            res.append(s[slow:fast])
            slow = fast
            fast = slow + 1
        return res