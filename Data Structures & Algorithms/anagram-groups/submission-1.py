from collections import defaultdict #HashMap + sorted string:
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list) #values-> list

        for word in strs:
            key= tuple(sorted(word))
            hashmap[key].append(word)
        return list(hashmap.values())
        """
        word
 ↓
sort characters
 ↓
use sorted characters as hashmap KEY
 ↓
append original word to the VALUE list
"""