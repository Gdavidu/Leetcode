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
# Merge Sorted Array
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for j in range(n):
            nums1[m+j] = nums2[j]
        nums1.sort()
#  Remove Duplicates from Sorted Array II
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentNum = 0
        count = 0
        k = 0
        for i in range(len(nums)):
            if nums[i] == currentNum:
                count+=1
            if nums[i] != currentNum:
                currentNum = nums[i]
                count=1
            if count<=2:
                nums[k] = nums[i]
                k+=1
        print nums
        return k
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tracker = defaultdict(int)
        for number in nums:
                tracker[number] += 1
        maxi = max(tracker.values())
        for key,value in tracker.items():
            if value == maxi:
                return key
# *Key notes: defaultdict(int) creates a dict that automatically assigns a default value of '0'
# for every nonexistant key, meaning you do not have to check a keys existence to increment it.
# This is a powerful tool for counting or accumulating values in a more succinct way.
# Additionally, this problem was a great review of remembering how to iterate over a dict
# using a comma in the notation to get both key and value from dict.items() sort of in a
# destructuring fashion

# Longest Common Prefix
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pointer = 0
        prefix = strs[0][0]
        print prefix
        for i in range(len(strs)):
            if prefix != strs[i][i]:
# solve
class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans=""
        v=sorted(v)
        first=v[0]
        last=v[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans
# Roman to Integer
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dictionary to keep track of how many of each roman numerals are in a string
        # if statement to check all 6 subtraction instances
        # delete each index where each subtraction is found, and the regularly found numerals after
        # counter variable so there is no need to loop thru dict and sole use of dict ... is nothing
        # scrap dict and only use if statements and counter to avoid having to loop thru dict

        # while loop that counts up all subtraction instances (conditional on whether the str
        # contains any of the instances)
        # another while loop looping thru str to count each value into a dict
        # an exp that adds up each value*its value and the prev loops count for the total
        count = 0
        while 'IV' in s or 'IX' in s or 'XL' in s or 'XC' in s or 'CD' in s or 'CM' in s:
            a=s.find('IV')
            if a!=-1:
                s = s.replace(s[a:a+1], '')
                count+=4
            b=s.find('IX')
            if b!=-1:
                s = s.replace(s[b:b+1], '')
                count+=9
            c=s.find('XL')
            if c!=-1:
                s = s.replace(s[c:c+1], '')
                count+=40
            d=s.find('XC')
            if d!=-1:
                s = s.replace(s[d:d+1], '')
                count+=90
            e=s.find('CD')
            if e!=-1:
                s = s.replace(s[e:e+1], '')
                count+=400
            f=s.find('CM')
            print(f)
            if f!=-1:
                s = s.replace(s[f:f+1], '')
                count+=900
        print('count: ', count, 'current s: ', s)
        count2 = 0
        while len(s)>0:
            if s[0] == 'M':
                count2+=1000
            if s[0] == 'D':
                count2+=500
            if s[0] == 'C':
                count2+=100
            if s[0] == 'L':
                count2+=50
            if s[0] == 'X':
                count2+=10
            if s[0] == 'V':
                count2+=5
            if s[0] == 'I':
                count2+=1
            s = s[1:]
            # print('count2: ', count2, 's: ', s)
        return count + count2
        #     if s[0] in tracker:
        #         tracker[s[0]]+=1
        #         del s[0]
        #     else:
        #         tracker[s[0]] = 1
        #         del s[0]
        # return count + 1000*tracker['M'] + 500*tracker['D'] + 100*tracker['C'] + 50*tracker['L'] + 10*tracker['X'] + tracker['I']

# ROMAN TO INT SOLVE
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dictionary to keep track of how many of each roman numerals are in a string
        # if statement to check all 6 subtraction instances
        # delete each index where each subtraction is found, and the regularly found numerals after
        # counter variable so there is no need to loop thru dict and sole use of dict ... is nothing
        # scrap dict and only use if statements and counter to avoid having to loop thru dict

        # while loop that counts up all subtraction instances (conditional on whether the str
        # contains any of the instances)
        # another while loop looping thru str to count each value into a dict
        # an exp that adds up each value*its value and the prev loops count for the total
        count = 0
        while 'IV' in s or 'IX' in s or 'XL' in s or 'XC' in s or 'CD' in s or 'CM' in s:
            a=s.find('IV')
            if a!=-1:
                s = s.replace('IV', '', 1)
                count+=4
            b=s.find('IX')
            if b!=-1:
                s = s.replace('IX', '',1)
                count+=9
            c=s.find('XL')
            if c!=-1:
                s = s.replace('XL', '',1)
                count+=40
            d=s.find('XC')
            if d!=-1:
                s = s.replace('XC', '',1)
                count+=90
            e=s.find('CD')
            if e!=-1:
                s = s.replace('CD', '',1)
                count+=400
            f=s.find('CM')
            if f!=-1:
                s = s.replace('CM', '',1)
                count+=900
        print('count: ', count, 'current s: ', s)
        count2 = 0
        while len(s)>0:
            if s[0] == 'M':
                count2+=1000
            if s[0] == 'D':
                count2+=500
            if s[0] == 'C':
                count2+=100
            if s[0] == 'L':
                count2+=50
            if s[0] == 'X':
                count2+=10
            if s[0] == 'V':
                count2+=5
            if s[0] == 'I':
                count2+=1
            s = s[1:]
        #     # print('count2: ', count2, 's: ', s)
        return count + count2
