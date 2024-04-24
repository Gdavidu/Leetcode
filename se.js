//Merge Sorted Array
//attempt 1 passes 13/59
var merge = function(nums1, m, nums2, n) {
    let index2 = n-1;

    for(let i=m+n-1; i>=0; i--){
        // console.log(m)
        if(m===0){
            console.log('hit')
            nums1[i]= nums2[index2]
            index2--
        }
        if(nums1[i]<nums2[index2] && nums1[i-1]<nums2[index2]){
        nums1[i]=nums2[index2]
         index2--
        }
        else if(nums1[i-1]>nums2[index2]){
            nums1[i] = nums1[i-1]
            nums1[i-1] = nums2[index2]
        }
        if(nums1[i]!=0 && nums1[i-1]>nums1[i]){
            let replace = nums1[i]
            nums1[i]= nums1[i-1]
            nums1[i-1] = replace
        }
    }
    return nums1
};
//attempt2 passes 30/59
var merge = function(nums1, m, nums2, n) {
    for(let i=0; i<m+n; i++){
        if(nums1[i]==0){
            nums1[i]=nums2[0]
            nums2.shift()
        }
        else if(nums1[i]>=nums2[0]){
            nums1.splice(i,0,nums2[0])
            nums1.pop()
            nums2.shift()
            console.log(nums1,nums2)
        }
    }
    return nums1
};

var merge = function(nums1, m, nums2, n) {
    let i = m - 1;
    let j = n - 1;
    let k = m + n - 1;

    while (j >= 0) {
        if (i >= 0 && nums1[i] > nums2[j]) {
            nums1[k--] = nums1[i--];
        } else {
            nums1[k--] = nums2[j--];
        }
    }
};

//Remove element
let i = 0;
for (let j = 0; j < nums.length; j++) {
    if (nums[j] !== val) {
        nums[i] = nums[j];
        i++;
    }
}
return i;
};    let i = 0;
for (let j = 0; j < nums.length; j++) {
    if (nums[j] !== val) {
        nums[i] = nums[j];
        i++;
    }
}
return i;
};

var romanToInt = function(s) {
    const romanValues = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    };

    let result = 0;

    for (let i = s.length - 1; i >= 0; i--) {
        const currValue = romanValues[s[i]];

        if (i < s.length - 1 && currValue < romanValues[s[i + 1]]) {
            result -= currValue;
        } else {
            result += currValue;
        }
    }

    return result;
};

//remove element(ez)
var removeElement = function(nums, val) {
    for(let i=0; i<nums.length; i++){
        if(nums[i]=== val) {
            nums.splice(i,1)
            i--
        }
    }
};

//majority element
var majorityElement = function(nums) {
    const n = nums.length;
    const map = new Map();

    for (const num of nums) {
        map.set(num, (map.get(num) || 0) + 1);
        if (map.get(num) > n / 2) {
            return num;
        }
    }
    return -1;
};
//test
HELLO HELLO

//remove duplicates (python)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
//find index of first occurence in string
var strStr = function(haystack, needle) {
    let n = haystack.length;
    let m = needle.length;

    if (m === 0) return 0; // empty needle

    for (let i = 0; i <= n - m; i++) {
        let found = true;
        for (let j = 0; j < m; j++) {
            if (haystack[i + j] !== needle[j]) {
                found = false;
                break;
            }
        }
        if (found) return i;
    }
    return false;
}
//majority element
//attempt 1
