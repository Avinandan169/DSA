int trap(int* height, int heightSize) {
    int total=0;
    int left_max=0,right_max=0;
    int left=0,right=heightSize-1;
    while(left<right){
        if(height[left]<=height[right]){
            if(left_max>height[left]){
                total+=left_max-height[left];
            }else{
                left_max=height[left];
            }
            left+=1;
        }else{
            if(right_max>height[right]){
                total+=right_max-height[right];
            }else{
                right_max=height[right];
            }
            right-=1;
        }
    }
    return total;
}