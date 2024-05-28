class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start, end = 0, 2
        if len(nums)<=2:
            return len(nums)
        k = len(nums)
        while end < len(nums) :
            print(nums)
            while nums[start] == nums[end] and nums[end] != '_':
                nums.pop(end)
                nums.append('_')
                k-= 1
            start += 1
            end += 1
        return k