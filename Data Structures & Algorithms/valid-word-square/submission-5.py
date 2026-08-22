class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        #check for kth row and kth col
        #kth row must match kth col
        #already given rows, we just need to check columns

        for i in range(len(words)):
            for j in range(len(words[i])):

                if j >= len(words):
                    return False

                if i >= len(words[j]):
                    return False

                if words[i][j] != words[j][i]:
                    return False
        
        return True