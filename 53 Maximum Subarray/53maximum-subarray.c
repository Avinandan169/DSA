int max(int a,int b){
    return (a > b) ? a:b;
}

int maxSubArray(int* nums, int numsSize) {
    int currsum=0;
    int maxsum=INT_MIN;
    for(int i=0; i<numsSize; i++){
        currsum+=nums[i];
        maxsum=max(currsum,maxsum);
        if( currsum<0 ){
            currsum=0;
        }
    }
    return maxsum;
}