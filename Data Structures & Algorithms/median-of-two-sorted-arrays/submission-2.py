class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return -1
        
        new = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                new.append(nums1[i])
                i += 1
            else:
                new.append(nums2[j])
                j += 1
        
        if i < len(nums1):
            new += nums1[i:]
        if j < len(nums2):
            new += nums2[j:]
        
        if len(new) % 2 == 1:
            return new[len(new) // 2]
        else:
            return (new[len(new) // 2] + new[len(new) // 2 - 1]) / 2