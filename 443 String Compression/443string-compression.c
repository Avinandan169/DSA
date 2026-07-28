int compress(char* chars, int charsSize) {
    int idx=0;
    char str[12];
    int n=charsSize;
    int i=0;
    while(i<charsSize){
        char chr=chars[i];
        int count=0;
        while(i<n && chars[i]==chr){
            count++;
            i++;
        }
        if(count==1) chars[idx++]=chr;
        else{
            snprintf(str,sizeof(str),"%d",count);
            int m=(int)strlen(str);
            chars[idx++]=chr;
            for(int j=0;j<m;j++){
                chars[idx++]=str[j];
            }
        }
    }
    return idx;
}