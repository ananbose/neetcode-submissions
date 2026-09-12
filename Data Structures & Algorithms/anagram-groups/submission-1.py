from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts={}
        for str1 in strs:
            str2 = "".join(sorted(str1))

            if str2 in dicts:
                dicts[str2].append(str1)
            else:
                dicts[str2] = [str1]
        result = []
        for v in dicts.values():
            result.append(v)
        return result

        