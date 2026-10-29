class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashMap = {}
        # for i in (nums):
        #     if i in hashMap:
        #         hashMap[i] += 1
        #     else:
        #         hashMap[i] = 1
        
        # sortedHash = {key: value for key, value in sorted(hashMap.items(), key=lambda item: item[1], reverse=True)}
        # return (list(sortedHash)[:k])

        count = {}
        freq =[[] for i in range(len(nums) + 1)]

        for n in (nums):
            count[n] = 1 + count.get(n,0)
        
        for n,c in count.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res



