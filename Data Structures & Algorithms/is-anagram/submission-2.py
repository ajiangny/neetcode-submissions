class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Anagram is true if they contain the same characters
        #that means we should count the number of characters
        #order does not matter
        count1 = defaultdict(int) #hashmap to track # of appearances of chars
        count2 = defaultdict(int)

        for c in s:
            if c not in count1:
                count1[c] = 1
            else:
                count1[c] += 1
            
        for c in t:
            if c not in count2:
                count2[c] = 1
            else:
                count2[c] += 1

        if count1 != count2:
            return False
        else:
            return True
