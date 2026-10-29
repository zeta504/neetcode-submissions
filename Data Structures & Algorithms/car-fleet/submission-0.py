class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet, lead = 0, 0
        cars = [(pos, vel) for pos, vel in zip(position, speed)]
        cars.sort(reverse=True)
        for pos, vel in cars:
            time = (target - pos) / vel
            if time > lead:
                fleet += 1
                lead = time
        return fleet
