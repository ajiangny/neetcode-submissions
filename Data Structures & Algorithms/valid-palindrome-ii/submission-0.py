class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        two pointers
        once we reach a difference, we can check two scenarios
        remove left or remove right
        """

        l, r = 0, len(s) - 1

        while l < r:
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return self.removeOnce(s, l + 1, r) or self.removeOnce(s, l, r - 1)

        return True

    def removeOnce(self, s, l, r):
        while l < r:
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True