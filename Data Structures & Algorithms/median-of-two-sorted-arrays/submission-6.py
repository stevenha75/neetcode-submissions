class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A # make A the smaller array

        # start binary search 
        l, r = 0, len(A) - 1

        # keep searching until we find median
        while True: # we know a median must exist 
            # calculating end index of left portion for both arrays
            ma = (l + r) // 2
            mb = half - ma - 2

            # checking validity of left portion
            # value after middle for ear subarray req for check
            Aleft = A[ma] if ma >= 0 else float("-infinity")
            Aright = A[ma + 1] if (ma + 1) < len(A) else float("infinity") 
            Bleft = B[mb] if mb >= 0 else float("-infinity")
            Bright = B[mb + 1] if (mb + 1) < len(B) else float("infinity") 

            # case: valid portions
            if Aleft <= Bright and Bleft <= Aright:
                # can now calc median
                if total % 2:
                    return min(Aright, Bright) 
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = ma - 1
            else: # B left > A right case
                l = ma + 1


