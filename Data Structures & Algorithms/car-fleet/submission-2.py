class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        count = 0
        fleet_cur = 0
        for p, s in pairs:
            t = (target - p) / s
            if t > fleet_cur:
                count += 1
                fleet_cur = t
        return count