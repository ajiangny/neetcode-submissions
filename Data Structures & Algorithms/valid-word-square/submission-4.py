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

                print(words[i][j] + str(i) + str(j) + " =? " + words[j][i] + str(j) + str(i))
                if words[i][j] != words[j][i]:
                    print("No")
                    return False
        
        return True