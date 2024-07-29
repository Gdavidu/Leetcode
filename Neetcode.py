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
#Notes:
# used a hashmap again but new concept: the get method for sets that checks whether the calue exists or sets the default value as 0. Kind of remember this concept but in a different syntax, gonna review some of my old leetcode solutions. Back
# to the solution: then using any of the two sets, check each value against the set of the other. I believe this means that hashsets are sorted? Nevermind its checking whether or not get returns a value cool.

# Two Integer Sum
# My halfworking, not sure why out of range solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        firstInd = 0
        for i in range(len(nums)):
            if (target-nums[i]) in nums:
                firstInd = i
                break
        numsSplit = nums[firstInd+1:]
        indDiff  = len(nums)-len(numsSplit)
        print(numsSplit)
        secondInd = numsSplit.index(target-nums[firstInd])
        return [firstInd, secondInd+indDiff]
# Theirs:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
# Notes Can use sets with the key and value being anything i.e the key can be the value of an element of i and the value can be index. Ik this but somehow wasnt first instinct on this problem
# Powerful use of enumerate() which returns a tuple of the index,value from nums or any type of iterable. Use of i,n to unpack the tuple thats returned

# Anagram Groups:
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        sortlist = []
        for str in strs:
            charLis = sorted(str)
            sortstr = ''.join(charLis)
            sortlist.append(sortstr)
        # print (sortlist)
        for i,n in enumerate(sortlist):
                ans[n].append(strs[i])
        return ans.values()
# Their Sol:
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()
# Notes: Use of a dict thats value is a list, learned to just append the value to a key because either way you are appending something to a new key or an existing.
# Their solution made use of a list of 0s and would increment the index of each 0 if the ascii value matched. They ensured the ascii value would match up to an index by subtracting each ascii value by the ascii val of a.
#  This made their solution a time complexity of m*n rather than my sol of m*nlogn because of the sort i employed. All in all, very creative way of making use of the key/value of a hashmap/set
# An additional note is that a list cannot be used as a key in sets but a tuple can in python
# Roman to Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        ans = 0

        for i in range(len(s)):
            if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
                ans -= m[s[i]]
            else:
                ans += m[s[i]]

        return ans
# Way better Roman to Integer code:
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        total = 0
        prev = 0
        for symbol in s[::-1]:
            if map[symbol] >= prev:
                total += map[symbol]
            else:
                total -= map[symbol]
            prev = map[symbol]
        return total
    # Notes: By iterating backwards you avoid the potential range error of the i+1 approach. The use of a map is a little new to me but its just like an object in JS. Iterate over a string backwards using the notation [::-1] where with no 'start', 'stop' but with a -1 step indicated, the list is just reversed. 
