class Solution:
    def merge(self, nums1:list, m: int, nums2:list, n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l1 = [ nums1[i] for i in range(0,m)]
        l2 = [ nums2[i] for i in range(0,n)]
        i = 0
        while len(l1) != 0 and len(l2)!=0:
            print(2)
            if l1[0] < l2[0]:
                nums1[i] = l1[0]
                l1.pop(0)  
            elif l1[0] >= l2[0]:
                nums1[i] = l2[0]    
                l2.pop(0)   
            i+=1
        
        while len(l1)!=0:
            nums1[i]=l1.pop(0)
            i+=1
        
        while len(l2)!=0:
            nums1[i]=l2.pop(0)
            i+=1
        
        return nums1

x = Solution()
print(x.merge([1,2,3,0,0,0],3,[2,5,6],3))