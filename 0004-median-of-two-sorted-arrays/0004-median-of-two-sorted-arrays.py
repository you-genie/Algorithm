class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        def findKth(nums1, nums2, k):
            if len(nums1) > len(nums2):
                return findKth(nums2, nums1, k)
            if not nums1:
                return nums2[k - 1]
            if k == 1:
                return min(nums1[0], nums2[0])

            i, j = min(k // 2, len(nums1)), min(k // 2, len(nums2))
            if nums1[i - 1] > nums2[j - 1]:
                return findKth(nums1, nums2[j:], k - j)
            else:
                return findKth(nums1[i:], nums2, k - i)

        total_len = len(nums1) + len(nums2)
        if total_len % 2 == 1:
            return findKth(nums1, nums2, total_len // 2 + 1)
        else:
            return (findKth(nums1, nums2, total_len // 2) +
                    findKth(nums1, nums2, total_len // 2 + 1)) / 2