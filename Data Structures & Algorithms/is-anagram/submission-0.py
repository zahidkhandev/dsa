class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return sorted(s) == sorted(t)
        
        # map1 = {}
        # map2 = {}

        # for i, v in enumerate(s):
        #     map1[v] = 0
        #     for j, x in enumerate(t):
        #         map2[x] =0

        # for i , v in enumerate(s):
        #     map1[]
        #     for j, x in enumerate(t):
