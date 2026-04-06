void merge(int* nums,int low,int mid,int high){
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
    while(i<n1) nums[k++]=left[i++];
    while(j<n2) nums[k++]=right[j++];
}
void mergesort(int* nums,int low,int high){
    if(low>=high) return;
    int mid=low+(high-low)/2;
    mergesort(nums,low,mid);
    mergesort(nums,mid+1,high);
    merge(nums,low,mid,high);
}

int majorityElement(int* nums, int numsSize) {
    mergesort(nums,0,numsSize-1);
    return nums[numsSize/2];
        
}