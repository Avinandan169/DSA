bool isPalindrome(int x) {
    if (x<0){
        return false;
    }
    long long n=x;
    int remainder=0;
    long long rev_num=0;
    while(n>0){
        remainder=n%10;
        rev_num=(rev_num*10)+remainder;
        n=n/10;
    }
    if (rev_num==x){
        return true;
    }
    else return false;   
}