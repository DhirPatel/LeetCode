class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        n = len(nums1)
        m = len(nums2)
        if n == 0:
            if m%2 != 0:
                return nums2[m//2]
            else:
                return ((nums2[(m//2)-1] + nums2[m//2])/2)
        if m == 0:
            if n%2 != 0:
                return nums1[n//2]
            else:
                return ((nums1[(n//2)-1] + nums1[n//2])/2)
        lst = []
        while i<n or j<m:
            if i >= n and j < m:
                lst.append(nums2[j])
                j += 1
            elif j >= m and i < n:
                lst.append(nums1[i])
                i += 1
            elif nums1[i] < nums2[j]:
                lst.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                lst.append(nums2[j])
                j += 1
            elif nums1[i] == nums2[j]:
                lst.append(nums1[i])
                lst.append(nums2[j])
                i += 1
                j += 1
        l = len(lst)
        if l%2==0:
            return ((lst[(l//2)-1] + lst[l//2])/2)
        else:
            return (lst[l//2])