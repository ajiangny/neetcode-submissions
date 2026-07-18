class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #nums2 i want to save the index in a dict
        #nums1 i want to go through and insert from numsDict into mapping
        mappings = []
        numsDict = {}

        for i in range(len(nums2)):
            numsDict[str(nums2[i])] = i
        
        for i in range(len(nums1)):
            mappings.append(numsDict[str(nums1[i])])
        
        return mappings