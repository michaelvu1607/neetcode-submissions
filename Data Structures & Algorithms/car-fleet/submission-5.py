class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = zip(position, speed)
        cars = sorted(cars, reverse=True)

        for pos, spd in cars:
            time = (target - pos) / spd

            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)