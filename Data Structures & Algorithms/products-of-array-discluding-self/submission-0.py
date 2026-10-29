class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        for i, v in enumerate(nums):
            for j, x in enumerate(nums):
                if i !=j :
                    res[i] = res[i] * x

        return (res)