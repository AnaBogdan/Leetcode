class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        ps = [1] * len(nums)
        pd = [1] * len(nums)
        pd[0] = nums[0]
        ps[- 1] = nums[-1]
        for i in range(1, len(nums) - 1):
            pd[i] = pd[i - 1] * nums[i]
        for i in range(len(nums) - 2, 0, -1):
            ps[i] = ps[i+1] * nums[i]
        for i in range(len(nums) - 1):
            ans[i] = pd[i-1] * ps[i+1]
        ans[len(nums) -  1] = pd[len(nums)-2]
        return ans

