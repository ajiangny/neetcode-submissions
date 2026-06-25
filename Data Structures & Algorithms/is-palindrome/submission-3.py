class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        we need two pointers
        compare left and right
        we want to ignore all non-alphanum chars, spaces, and case
        """

        l = 0
        r = len(s) - 1
        s = s.lower()

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True
