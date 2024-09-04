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
# *every loop creates a new 26-long list of 0s that will uniquely identify the letters in words by incrementing certain indices by the ascii value diff between the char and the ascii value of 'a'

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
# Top K elements in list *got to hashmap part but could not figure out
# Sol
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            count[num] = 1 + count.get(num,0)
        for num, c in count.items():
            freq[c].append(num)
        print(count, freq)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
# Notes Figured out that I needed a hashmap to count the occurences of each value and used .items to access them but past that, I went a bad route of trying to sort and push the keys into an ans list which was time complexity wasteful and would not work. The solution once again was multiple arrays inside an array in which each array represented how frequent each value would occur, so it autosorted. The efficiency in this solution is in how it caps te length of the list we need to sort by using the length of the input list (since the freq will never exceed the input list )

# String encode and decode
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res
# Daily Challenge: Magic Squares In Grid
class Solution(object):
    def magicCheck(self, square):
        if len(set(square)) != 9:
            return False
        if min(square)<1 or max(square)>9:
            return False
        sum1 = square[0] + square[1] + square[2]
        # rows
        if square[0] + square[1] + square[2] != sum1:
            return False

        if square[3] + square[4] + square[5] != sum1:
            return False

        if square[6] + square[7] + square[8] != sum1:
            return False

        # columns
        if square[0] + square[3] + square[6] != sum1:
            return False

        if square[1] + square[4] + square[7] != sum1:
            return False

        if square[2] + square[5] + square[8] != sum1:
            return False

        # diagonals
        if square[0] + square[4] + square[8] != sum1:
            return False

        if square[2] + square[4] + square[6] != sum1:
            return False

        return True
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        c = len(grid)
        r = len(grid[0])
        if c<3 or r<3:
            return res
        for i in range(c-2):
            for j in range(r-2):
                if self.magicCheck(grid[i][j:j+3]+grid[i+1][j:j+3]+grid[i+2][j:j+3]):
                    # print(grid[i][j:j+3]+grid[i+1][j:j+3]+grid[i+2][j:j+3])
                    res +=1
        return res
# Notes: Definitely a trip for me conceptualizing and something I hope will improve
# over more problems. Got stuck trying to figure out how to iterate over a 9 window
# square of the grid and was able to attack the problem through a double for loop
# suggested by Sat. If the length of the row is the boundary of the index +1, a range
# of len(row)-2 will start from 0 and only go to an index +3 that is in range of the
# input grid. ex.) a grid row w length 6 will have a range(4)-> 0,1,2,3 and 3,
# included, will only require the last index 5 to create a 3x3. An additional tool
# I learned was how to create a separate method for modularity and readability. A
# huge brunt of my brute force is stuffed into the magicCheck method and separates
# my grid parsing from my magic square checking.

# Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False

        return True
# Product of Array Discluding Self
# Mine
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if j != i:
                    product = product*nums[j]
            res.append(product)
        return res
# Theirs:
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
# Notes
#
# Valid Sudoku
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True

# Design a class that:
# 1. can addd a value(no dupes)
# 2. can remove a value
# 3. gets a random value from already inserted values with equal probability

class Store:
    def __init__(self):
        self.map = set()
    def insert(self, value):
        self.map.add(value)
    def remove(self,value):
        self.map.remove(value)
    def getRand(self):
        return random.choice(list(map))
# Is Palindrome
# Note: cheat way using built-in python functions such as string.isalnum() to filter out nonalphanumeric characters
# string.lower() to convert to lowercase
# Notes on proper Solution: Two pointers, one at each side. stop conditional on whther the pointers have met or passed each other.
# Use ASCII symbol to filter out nonalphanumerics in a helper function that returns a bool if the ord(char) is between the values for ord(A-Z,a-z, or 0-9)
# My solution (less efficient with memory/storage because of the extra variables):
class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = self.alphaNumFilter(s)
        reverse = ''
        for i in range(len(filtered)-1, -1, -1):
                # print(i)
                reverse+= filtered[i]
        print(reverse)
        # print(self.alphaNumFilter(s), self.alphaNumFilter(reverse))
        return reverse == filtered
    def alphaNumFilter(self, word: str):
        res = ''
        for i in word:
            if i.isalnum():
                res+= i.lower()
        return res
# Notes: Could have saved major time by using str[::-1] to obtain the reversed str but also learned how to use range(starting:end:step)
# refreshing the face that the starting point for range() is inclusive and the end is exclusive.
# Their Suboptimal solution:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''
        for c in s:
            if c.isalnum():
                res += c.lower()
        return res == res[::-1]
# Notes: Way simpler than mine and completely gaps the way I approached the problem

# Thier Optimal SOlution that is peak memory conservative and minimal time complexity:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
# Notes: Since the suboptimal solution concatenates each char to the string, a new str
# is created each time since strs are immutable. This results in a higher usage of memory
# and in the worst case a time complexity that comes closer to O^(n^2)

