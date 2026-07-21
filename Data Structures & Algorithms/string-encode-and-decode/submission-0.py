class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for string in strs:
            encoded_string += str(len(string)) + '#' + string

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        j = 0
        while i < len(s):
            if s[j] == '#':
                length = int(s[i:j])
                decoded_strs.append(s[j + 1:j + 1 + length])
                i = j + 1 + length
                j = i
            else:
                j += 1

        return decoded_strs