'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            n=nums.count(i)
            if n>len(nums)//2:
                return i
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=0
        val=nums[0]
        for i in nums:
            if c==0:
                val=i
            if val==i:
                c+=1
            else:
                c-=1
        return val
