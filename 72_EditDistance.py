# Edit distance of two words. Dynmaic programming
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        vals = {}
        def solve(w1, w2):
            if len(w1) == 0 or len(w2) == 0:
                vals[(w1,w2)] = max(len(w1), len(w2))
                return vals[(w1,w2)]
            if (w1,w2) in vals:
                return vals[(w1,w2)]
            if w1[0] == w2[0]:
                vals[(w1,w2)] = solve(w1[1:], w2[1:])
                return vals[(w1,w2)]
            replace = 1 + solve(w1[1:], w2[1:])
            delete = 1 + solve(w1[1:], w2) 
            insert = 1 + solve(w1, w2[1:])
            vals[(w1,w2)] =  min(replace, delete, insert)
            return vals[(w1,w2)]
        return solve(word1, word2)