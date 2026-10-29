class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for i in (nums):
            if i in hashMap:
                hashMap[i] += 1
            else:
                hashMap[i] = 1
        
        sortedHash = {key: value for key, value in sorted(hashMap.items(), key=lambda item: item[1], reverse=True)}
        return (list(sortedHash)[:k])

