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
