from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we want to return a list of lists
        #create a map

        anagram_map = defaultdict(list)

        for string in strs:
            anagram_map[tuple(sorted(string))].append(string)
        
        return list(anagram_map.values())
