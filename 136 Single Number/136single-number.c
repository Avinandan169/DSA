int singleNumber(int* nums, int numsSize) {
    for(int i=0;i<numsSize;i++){
        int check=0;
        for (int j=0;j<numsSize;j++){
            if(nums[i]==nums[j]){
                check+=1;
            }
        }
        if(check==1){
            return nums[i];
        }
    }
    return 0;
}