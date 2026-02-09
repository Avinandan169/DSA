int reverse(int x){
    long rem=0,rev=0,num=x;
    if(num>0){
        while (num>0){
            rem=num%10;
            rev=(rev*10)+rem;
            num/=10;
        }
    }
    else{
        while (num<0){
            rem=num%10;
            rev=(rev*10)+rem;
            num/=10;
        }


    }
    if (rev>INT_MAX || rev<INT_MIN) return 0;
    else return rev;
}