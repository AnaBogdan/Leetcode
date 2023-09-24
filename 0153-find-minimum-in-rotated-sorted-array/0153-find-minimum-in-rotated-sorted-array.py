class Solution:
    def findMin(self, nums: List[int]) -> int:
        r = len(nums)-1
        l = 0
        #mid = len(nums) // 2
        minim = float("inf")
        
        while l < r:
            mid = (l+r)//2
            minim = min(minim, nums[mid])
            if nums[mid] > nums[r]: 
                l = mid + 1
            else:
                r = mid - 1
        return min(minim, nums[l])
