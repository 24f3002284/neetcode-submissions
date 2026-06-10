class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B=nums1,nums2
        total = len(A)+len(B)

        # we want to search do binary search in the smaller array
        if len(A)>len(B):
            A,B=B,A # swap

        half=total//2
        Belements=total-half

        l,r=0,len(A)-1

        # median of each of the sorted arrays
        while True:
            i=(l+r)//2 # mid index of A
            j=half-i-2 # subtract 1 from half to get the reqd index, subtract 1 from i to get reqd index

            Aleft=A[i] if i>=0 else float('-inf')
            Aright=A[i+1] if (i+1)<len(A) else float('inf')
            Bleft=B[j] if j>=0 else float('-inf') # not =B[i], but B[j]
            Bright=B[j+1] if j+1<len(B) else float('inf')

            if Aleft<=Bright and Bleft<=Aright:
                if total%2==0:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2
                else:
                    return min(Aright,Bright)

            elif Bleft>Aright:
                # j-=1
                # i+=1
                l=i+1
            else:
                # j+=1
                # i-=1
                r=i-1

        
