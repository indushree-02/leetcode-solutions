class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if k==n:
            return max(nums)
        arr=[]
        if k==1:
            for i in nums:
                if nums.count(i)==1:
                    arr.append(i)
        else:
            if nums.count(nums[0])==1:
                arr.append(nums[0]) 
            if nums.count(nums[-1])==1:
                arr.append(nums[-1])
        if arr:
            return max(arr)
        else:
            return -1
