class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            ind=nums.index(target)
            return ind
        else:
            return -1