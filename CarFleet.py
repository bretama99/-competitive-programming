class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed))
        ans = []
        length = len(cars)
        for i in range(length-1,-1,-1):
            # get the time to reach the target
            pos,sp = cars[i]
            time = (target-pos)/sp
            if not ans or time>ans[-1]:
                ans.append(time)
        return len(ans)
            
