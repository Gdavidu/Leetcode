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
