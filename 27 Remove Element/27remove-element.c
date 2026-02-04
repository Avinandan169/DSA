int removeElement(int* nums, int numsSize, int val) {
    int expectedNums[100];
    int index=0;
    for (int i=0;i<numsSize;i++){
        if (nums[i]!=val){
            expectedNums[index++]=nums[i];

        }
    }
    int k=index;
    for(int i=0;i<index;i++){
        nums[i]=expectedNums[i];
    }
    return k;
}