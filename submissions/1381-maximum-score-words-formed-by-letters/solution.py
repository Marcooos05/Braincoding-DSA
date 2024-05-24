import copy
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        memo = [0] * len(words)

        def dp(n, limit):
            left = copy.deepcopy(limit)
            if n == len(words):
                return 0
            #if memo[n]:
            #    return memo[n]
            else:
                reward = 0
                for char in words[n]:
                    if char not in left:
                        reward = 0
                        break
                    left.remove(char)
                    reward += score[ord(char)-97]
                m = max(dp(n+1,limit), reward + dp(n+1, left))
                memo[n] = m
                return m
        dp(0,letters)
        return memo[0]
