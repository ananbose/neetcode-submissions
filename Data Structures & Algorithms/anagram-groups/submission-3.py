from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for i in strs:
            count = Counter(i)
            key = tuple(sorted(count.items()))

            if key in anagram:
                anagram[key].append(i)
            else:
                anagram[key]=[i]
        result = []
        for i in anagram.values():
            result.append(i)
        return result
