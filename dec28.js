// Dec 12 2023 Prac

// Two Sum (easy)
// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.
// Example 1:
// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
// Example 2:
// Input: nums = [3,2,4], target = 6
// Output: [1,2]
// Example 3:
// Input: nums = [3,3], target = 6
// Output: [0,1]
// Constraints:
// 2 <= nums.length <= 104
// -109 <= nums[i] <= 109
// -109 <= target <= 109
// Only one valid answer exists.

const TwoSum = function(nums,target){
    for(let i=0; i<nums.length; i++){
        const val = target-nums[i]
        if(nums.includes(val) && !(nums.indexOf(val)===i)){
            return [i,nums.indexOf(val)]
        }
    }
}

const nums = [2,7,11,15]
const target = 9
// console.log(TwoSum(nums,target))

//Palindrome Number
//Given an integer x, return true if x is a palindrome , and false otherwise.
const Palindrome = function(x){
    const str = x.toString()
    const reversedArr = str.split('').reverse()
    const reversed = reversedArr.join('')
    return str === reversed
}
let x = 121
console.log(Palindrome(x))

// Longest Common Prefix
// Write a function to find the longest common prefix string amongst an array of strings.

// If there is no common prefix, return an empty string "".

// Example 1:

// Input: strs = ["flower","flow","flight"]
// Output: "fl"
// Example 2:

// Input: strs = ["dog","racecar","car"]
// Output: ""
// Explanation: There is no common prefix among the input strings.


// Constraints:

// 1 <= strs.length <= 200
// 0 <= strs[i].length <= 200
// strs[i] consists of only lowercase English letters.

var longestCommonPrefix = function(strs) {
    let str = strs[0]
    for (let word of strs){
        while(word.indexOf(str) !== 0) {
            str = str.slice(0,-1)
            if (str === '') return ''
        }
    }
    return str

};
