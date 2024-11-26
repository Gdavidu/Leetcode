# Contains Duplicate
#  My sol:
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        while len(nums)>0:
            x =  nums.pop(0)
            if x in nums:
                return True
        return False
# Theirs:
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
# Notes:
# My solution is O(n^2) because each iteration requires a pop and x in nums
# which are both O(n) operations. When I saw that the question was asking after
# duplicates, I should have immediately thought of a hash set.
