import collections
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag_dict = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord("a")] +=1
            anag_dict[tuple(count)].append(s)
        return list(anag_dict.values())
