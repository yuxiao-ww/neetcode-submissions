class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return 0

        new = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                new.append(nums1[i])
                i += 1
            else:
                new.append(nums2[j])
                j += 1
        
        if i < len(nums1):
            new += nums1[i:]
        if j < len(nums2):
            new += nums2[j:]

        n = len(new)
        if n % 2 == 1:
            return new[n//2]
        else:
            return (new[n//2] + new[n//2-1]) / 2