class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indices = []
        for i, v in enumerate(nums):
            if indices != []:
                return indices
            for j, x in enumerate(nums):
                if i != j:
                    if v+x == target:
                        indices = [i, j]
                        break
        return indices