from typing import List

# Duplicate Integer:
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
# My solution:

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            print(i)
            if nums[i] == nums[i+1]:
                return True
        return False

# Test cases:
# nums = [1, 2, 3, 3]
# print(Solution().hasDuplicate(nums))

# Theirs:
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         hashset = set()

#         for n in nums:
#             if n in hashset:
#                 return True
#             hashset.add(n)
#         return False
# Notes:
# Using a hashmap you sacrifice space complexity for an O(n) time complexity. My solution is a O(nlog(n)) but by using a hashsetto chekc values against, you achieve a O(n) time comp and a O(n) space comp as opposed to the prev O(1) space comp.
# This solution entails checking whether the value is in the hashset and inputting it in the hashset if it isnt

# Is Anagram
# My Sol:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sList = list(s)
        tList = list(t)
        sList.sort()
        tList.sort()
        if len(tList) != len(sList):
            return False
        for i in range(len(sList)):
            if sList[i] != tList[i]:
                return False
        return True
# Theirs:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
