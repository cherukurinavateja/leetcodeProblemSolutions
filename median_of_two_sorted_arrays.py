import math
class Solution:
    
    
    def med(a): 
        
        if len(a) % 2 == 0:
            n1,n2=int(len(a)/2)-1,int(len(a)/2)
            med_a=(a[n1]+a[n2])/2
            return med_a
        else:
            num=math.ceil(len(a)/2)-1
            med_a=a[num]
            return med_a
    
    
    def findMedianSortedArrays(self, nums1, nums2):
        if (len(nums1) >0) and (len(nums2)>0):
            nums1.extend(nums2)
            nums1.sort()
            median=Solution.med(nums1)
            return median
        elif (len(nums1) >0) and (len(nums2)==0):
            median=Solution.med(nums1)
            return median
        elif (len(nums1) == 0) and (len(nums2) > 0):
            median=Solution.med(nums2)
            return median
        else:
            return 0