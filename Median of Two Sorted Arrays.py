class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list):
        index = len(nums1) + len(nums2)
        endIndex = int(index/2)
        l = []
        while len(nums1)!=0 and len(nums2)!=0: 
            if nums1[0] <= nums2[0]:
                x = nums1.pop(0)
                l.append(x) 
            elif nums1[0] >= nums2[0]:
                x = nums2.pop(0)
                l.append(x)
            if len(l) > endIndex:
                break
        
        while len(nums1)!=0:
            x = nums1.pop(0)
            l.append(x)
        
        while len(nums2)!=0:
            x = nums2.pop(0)
            l.append(x)      
        
        if index%2 == 0:
            return (l[endIndex]+l[endIndex-1])/2  
        else :
            return l[endIndex]  
            

x  = Solution()
print(x.findMedianSortedArrays([1,2],[3,4]))
print(x.findMedianSortedArrays([1,3],[2]))
print(x.findMedianSortedArrays([1,3,4],[2]))