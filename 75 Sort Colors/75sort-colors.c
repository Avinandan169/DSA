void swap(int* nums,int index1, int index2){
    int temp=nums[index1];
    nums[index1]=nums[index2];
    nums[index2]=temp;
}
void sortColors(int* nums, int numsSize) {
    int low=0;
    int mid=0;
    int high=numsSize-1;
    while(mid<=high){
        if(nums[mid]==0){
            swap(nums,low,mid);
            low++;
            mid++;
        }
        else if(nums[mid]==1){
            mid++;
        }
        else{                   // (nums[mid]==2)
            swap(nums,mid,high);
            high--;
        }
    }
}