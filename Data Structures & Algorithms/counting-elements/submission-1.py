class Solution:
    def countElements(self, arr: List[int]) -> int:
        # first put array into a map
        # then we loop thru array to check if the arr[i] + 1 exists in the map

        arr_map = set(arr)
        count = 0

        for i in range(len(arr)):
            if arr[i] not in arr_map:
                arr_map[i] = arr[i] + 1 #this is grabbing the arr # and adding it

        #loop thru array. if it exists, remove it so we don't overcount
        for i in range(len(arr)):
            check = arr[i] + 1
            if check in arr_map:
                count += 1

        return count