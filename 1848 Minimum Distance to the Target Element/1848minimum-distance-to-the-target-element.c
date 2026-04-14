int getMinDistance(int* nums, int numsSize, int target, int start) {
    int up=-1,down=-1,i,j;
    for(i=start;i<numsSize;i++){
        if(nums[i]==target){
            up=i-start;
            break;
        }
    }
    for(j=start;j>=0;j--){
        if(nums[j]==target){
            down=start-j;
            break;
        }
    }
    if(up==-1) return down;
    else if(down==-1 || up<down) return up;
    else return down;
    
}