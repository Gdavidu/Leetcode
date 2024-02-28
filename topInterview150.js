//Merge Sorted Array

var merge = function(nums1, m, nums2, n) {

    for(let i=0; i<m*2; i++){
        if(nums1[i]>=nums2[0]){
            nums1.splice(i,0,nums2[0])
            nums2.pop()
            i++
            nums1.pop()
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
