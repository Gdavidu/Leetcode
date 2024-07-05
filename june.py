# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal
# substring
#  consisting of non-space characters only.

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        slist = s.split()
        print slist
        return len(slist[-1])
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in nums:
            if i == val:
                nums.remove(i)
        print nums
        return len(nums)
    # WHY NO WORK

# Merge Sorted Arrays Refresh:
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.



# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        a = m-1
        b = n-1
        c = m+n-1
        while b>=0:
            if a>=0 and nums1[a]>nums2[b]:
                nums1[c] = nums1[a]
                a-= 1
            else:
                nums1[c] = nums2[b]
                b-= 1
            c-=1

# Remove Duplicates from Sorted Array
# Solution using python built-in methods:
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums[:] = set(nums)
        nums.sort()
        return len(nums)
# Solve
class Solution(object):
    def removeElement(self, nums, val):
        pointer = len(nums) -1
        while pointer >= 0:
            if nums[pointer] == val:
                nums.pop(pointer)
            pointer-=1
        return len(nums)
