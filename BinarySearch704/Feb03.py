class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while(l < r):
            m = l + (r - l)//2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1

ans = Solution()
print(ans.search([-1,0,3,5,9,12], 9))