class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        hashmap representing char frequency?
        count freq of each char in string
        turn count into key and append string to list w key
        """
        result = defaultdict(list)

        for string in strs:
            count = [0] * 26

            for c in string:

                count[ord(c) - ord('a')] += 1

            result[tuple(count)].append(string)

        return list(result.values())
