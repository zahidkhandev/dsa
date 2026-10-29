class Solution:
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     hashMap = {}
    #     finalList = []
    #     subList = {}

    #     for i, v in enumerate(strs):
    #         sortedValue = sorted(v)
    #         strSortedValue = ''.join(sortedValue)
    #         # if strSortedValue in hashMap:
    #         subList.setdefault(strSortedValue, []).append(v)
    #         # else:
    #         #     subList[strSortedValue] = subList[strSortedValue].append(v)

            
    #         # finalList.append(subList)
    #         # print(hash)
        
    #     finalList = list(subList.values())
    #     return finalList

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashMap = defaultdict(list)

        for i in strs:
            count = [0] * 26
            for j in i:
                count[ord(j) - ord("a")] += 1
            
            hashMap[tuple(count)].append(i)
        
        return list(hashMap.values())
