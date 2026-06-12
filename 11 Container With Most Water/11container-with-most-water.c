int min(int a,int b){
    return (a > b) ? b : a;
}
int max(int a,int b){
    return (a > b) ? a : b;
}

int maxArea(int* height, int heightSize) {
    int lp=0, rp=heightSize-1 ,ans=0;
    int width,min_height,curr_water,max_water=0;
    while(lp<rp){
        width=rp-lp;
        min_height=min(height[lp],height[rp]);
        curr_water= width * min_height;
        max_water=max(curr_water,max_water);
        height[lp] < height[rp] ? lp++ : rp--;
    }
    return max_water;
}