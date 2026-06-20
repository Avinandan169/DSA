void swap(int*nums, int a,int b){
    int temp=nums[b];
    nums[b]=nums[a];
    nums[a]=temp;
}
void reverse(int* nums,int numsSize){
    int i=0;
    int j=numsSize-1;
    while(i<j){
        swap(nums,i,j);
        i++;
        j--;
    }

}
void nextPermutation(int* nums, int numsSize) {
    int pivot=-1;
    for(int i=numsSize-2;i>=0;i--){
        if(nums[i]<nums[i+1]){
            pivot=i;
            break;
        }
    }

    if(pivot==-1){
        reverse(nums,numsSize);
        return;
    }

    for(int i=numsSize-1;i>pivot;i--){
        if(nums[i]>nums[pivot]){
            swap(nums,i,pivot);
            break;
        }
    }
    int i=pivot+1;
    int j=numsSize-1;
    while(i<j){
        swap(nums,i,j);
        i++;
        j--;
    }
}