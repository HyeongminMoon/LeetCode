class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_length = len(nums1) + len(nums2)
        if total_length % 2 == 1:
            return self.find_kth_small_num(nums1, nums2, total_length // 2)
        else:
            return (self.find_kth_small_num(nums1, nums2, total_length // 2) + self.find_kth_small_num(nums1, nums2, total_length // 2 - 1)) / 2.
    
    def find_kth_small_num(self, A: List[int], B: List[int], k: int):
        """
            split each array into two.
            A => {LeftA}, pivotA, {RightA}
            B => {LeftB}, pivotB, {RightB}
        
            Step1.
            if pivotA > pivotB, we can confirm
                {LeftB}, ... , pivotB, ... , pivotA, ... , {RightA}
            
            else, we can confirm
                {LeftA}, ... , pivotA, ... , pivotB, ... , {RightB}
                
            Step2.
            now let's find kth number. assume pivotA > pivotB case.
            if k > sizeof(LeftA + LeftB), k is locate in []
                {LeftB}, ...(same amount as LeftA) , [... , pivotB, ... , pivotA, ... , {RightA}]
            so we can remove {LeftB}
            else, with the same reason we can remove {RightA}.
            
            The pivotB >= pivotA case flows same.
        
        """
        if not A:
            return B[k]
        if not B:
            return A[k]
        ind_pivotA, ind_pivotB = len(A) // 2 , len(B) // 2
        pivotA, pivotB = A[ind_pivotA], B[ind_pivotB]

        if pivotA > pivotB:
            if ind_pivotA + ind_pivotB < k:
                # remove {LeftB}
                return self.find_kth_small_num(A, B[ind_pivotB + 1:], k - (ind_pivotB + 1))
            else:
                # remove {RightA}
                return self.find_kth_small_num(A[:ind_pivotA], B, k)
        else:
            if ind_pivotA + ind_pivotB < k:
                # remove {LeftA}
                return self.find_kth_small_num(A[ind_pivotA + 1:], B, k - (ind_pivotA + 1))
            else:
                # remove {RightB}
                return self.find_kth_small_num(A, B[:ind_pivotB], k)