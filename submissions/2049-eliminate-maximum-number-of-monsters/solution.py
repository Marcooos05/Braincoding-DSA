class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        steps = []
        count = 0
        for i in range(len(dist)):
            step = dist[i] / speed[i]
            steps.append(step)
        steps.sort()


        for i in range(len(dist)):
            if steps[i] <= i:
                return i
        
        return len(steps)



        
