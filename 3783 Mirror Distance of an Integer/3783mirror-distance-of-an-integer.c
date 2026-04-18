int mirrorDistance(int n) {
    int rev_num=0;
    int num=n,rem;
    while(num>0){
        rem=num%10;
        rev_num=(rev_num*10)+rem;
        num=num/10;
    }
    return abs(n-rev_num);
}