class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # very simple, add the nums2 to the nums1 and just use the sort() funtion
        nums1[m:]= nums2
        nums1.sort()