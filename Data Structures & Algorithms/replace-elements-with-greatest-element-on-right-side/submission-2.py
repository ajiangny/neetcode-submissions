class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i in range(len(arr) - 1):
            greatestIndex = i + 1
            print("Current Index = " + str(i))
            print("Greatest Index = " + str(greatestIndex) + " is " + str(arr[greatestIndex]))
        
            for j in range(greatestIndex, len(arr)):
                if arr[greatestIndex] < arr[j]:
                    greatestIndex = j

            print("Index at " + str(arr[i]) + " changes to num at Greatest Index: " + str(arr[greatestIndex]))
            arr[i] = arr[greatestIndex]
            
        
        arr[-1] = -1

        return arr

            