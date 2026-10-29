class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapping = {}
        for i,v in enumerate(nums):
            mapping[v] = 0
            for j, x in enumerate(nums):
                if v == x:
                    mapping[v] += 1
        
        print(mapping)

        return any(value > 1 for value in mapping.values())
        