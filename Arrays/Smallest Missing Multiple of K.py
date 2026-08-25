class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        seen = set(nums)

        cur = k
        while cur in seen:
            cur += k

        return cur
