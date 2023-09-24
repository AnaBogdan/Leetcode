class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        diff = [0] * (len(nums) - 1)
        m = len(nums)
        if m > 0:
            n = heapq.heappop(nums)
        else:
            return 0
        for i in range(m-1):
            m = heapq.heappop(nums)
            if m - n == 1:
                diff[i] = 1
            elif m - n == 0:
                diff[i] = 2
            n = m
        #return nums
        c = 0
        #return diff
        index = []
        for i in range(len(diff)):
            if diff[i] == 1:
                c = c + 1
            elif diff[i] == 0 and c > 0:
                index.append(c)
                c = 0

# Handle the case when the last element of diff is 1
        if c > 0:
            index.append(c)

        return max(index)+1 if index else 1
