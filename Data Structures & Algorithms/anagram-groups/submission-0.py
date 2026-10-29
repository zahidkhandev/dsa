class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        finalList = []
        subList = {}

        for i, v in enumerate(strs):
            sortedValue = sorted(v)
            strSortedValue = ''.join(sortedValue)
            # if strSortedValue in hashMap:
            subList.setdefault(strSortedValue, []).append(v)
            # else:
            #     subList[strSortedValue] = subList[strSortedValue].append(v)

            
            # finalList.append(subList)
            # print(hash)
        
        finalList = list(subList.values())
        return finalList
