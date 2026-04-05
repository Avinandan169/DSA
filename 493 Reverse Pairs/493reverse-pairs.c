void merge(int *nums,int low,int mid,int high){
    int n1=mid-low+1;
    int n2=high-mid;
    int left[n1],right[n2];
    for(int i=0;i<n1;i++) left[i]=nums[low+i];
    for(int j=0;j<n2;j++) right[j]=nums[mid+j+1];
    int i=0,j=0,k=low;
    while(i<n1 && j<n2){
        if(left[i]<=right[j]) nums[k++]=left[i++];
        else nums[k++]=right[j++];
    }
    while(i < n1){
        nums[k++]=left[i++];
    }
    while(j<n2){
        nums[k++]=right[j++];
    }
}

int counting_pairs(int *nums,int low,int high){
    if (low>=high) return 0;
    int mid=low+(high-low)/2;
    int count=counting_pairs(nums,low,mid)+counting_pairs(nums,mid+1,high);

    int j=mid+1;
    for(int i=low;i<=mid;i++){
        while (j<=high && (long long)nums[i]>2*(long long)nums[j]){
            j++;
        }
        count+=(j-(mid+1));
    }
    merge(nums,low,mid,high);
    return count;
}

int reversePairs(int* nums, int numsSize) {
    return counting_pairs(nums,0,numsSize-1);
}