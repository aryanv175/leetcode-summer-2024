class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1 = {}
        n = len(nums)
        for num in nums:
            if num not in dict1.keys():
                dict1[num] = 1
            else:        
                dict1[num] += 1
        print(dict1)
        for num in dict1.keys():
            if dict1[num]>n//2:
                return num