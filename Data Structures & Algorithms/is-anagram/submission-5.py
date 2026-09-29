class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        anagram_map = {}

        for c in s:
            anagram_map[c] = anagram_map.get(c, 0) + 1

        for c in t:
            anagram_map[c] = anagram_map.get(c, 0) - 1
        
        return all(val == 0 for val in anagram_map.values())
    