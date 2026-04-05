int singleNonDuplicate(int* nums, int numsSize) {
    int i=0;
    while(i<numsSize-1){
        if(nums[i+1]!=nums[i]){
            return nums[i];
        }else{
            i+=2;
        }
    }
    return nums[i];
}