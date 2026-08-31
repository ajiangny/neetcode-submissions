class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        #We have a keyboard of len 26 (0 to 25)
        #Finger starts at 0
        #We are looking for the time from index i to index j |i - j|

        #Use the keyboard to type a string word

        keyboard_map = defaultdict(int) #put all the keys into a map pertaining to the index
        for c in range(len(keyboard)):
            keyboard_map[keyboard[c]] = c
        
        #starting from 0, we get the first char of word
        #we need to add the index distance
        total = 0
        start = 0

        for c in word:
            target = keyboard_map[c]
            distance = abs(start - target)
            total += distance
            start = target
        

        return total