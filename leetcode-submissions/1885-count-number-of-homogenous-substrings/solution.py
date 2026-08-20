class Solution:
    def countHomogenous(self, s: str) -> int:
        
        homo = s[0]
        result = 1

        for char in s[1:]:
            if char in homo:
                homo = homo + char
                result += len(homo)
            else:
                homo = char
                result += 1
        return int(result % (10**9 + 7))


