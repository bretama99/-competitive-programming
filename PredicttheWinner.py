class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        counts = defaultdict(int)
        cache = {}
        def maxScore(turn=0, left=0, right=len(nums)-1):
            state = (turn, left, right)
            if state in cache:
                return cache[state]

            # counts[(turn, left, right)] += 1
            if left == right:
                if turn:
                    cache[state] = 0
                    return cache[state]
                cache[state] = nums[left]
                return cache[state]
            if turn == 0:
                leftPath = nums[left] + maxScore(1, left+1, right)
                rightPath = nums[right] + maxScore(1, left, right-1)
                cache[state] = max(leftPath, rightPath)
            else:
                leftPath = maxScore(0, left+1, right)
                rightPath = maxScore(0, left, right-1)
                cache[state] = min(leftPath, rightPath)
            return cache[state]
        totalSum = sum(nums)
        player1MaxScore = maxScore()
        # for key, value in counts.items():
            # print("the subproblem ", key, " was calculated", value, " times")
        if player1MaxScore >= totalSum/2:
            return True
        return False 

        
