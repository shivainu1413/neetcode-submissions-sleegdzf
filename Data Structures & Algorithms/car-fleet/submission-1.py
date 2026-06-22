class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        fleets = 0
        pairs = sorted(zip(position, speed), reverse=True)
        for p, s in pairs:
            t = (target - p) / s
            if stack:
                if t > stack[-1]:
                    stack.append(t)
                    fleets += 1
            else:
                stack.append(t)
                fleets += 1
        return fleets
