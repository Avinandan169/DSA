bool isFreqSame(int* arr,int* arr1){
    for(int i=0;i<26;i++){
        if(arr[i]!=arr1[i]){
            return false;
        }
    }
    return true;
}

bool checkInclusion(char* s1, char* s2) {
    int freq[26]={0};
    int n1=(int)strlen(s1);
    int n2=(int)strlen(s2);
    
    if(n1>n2) return false;

    for(int i=0;i<n1;i++){
        freq[s1[i]-'a']++;
    }

    for(int i=0;i<n2;i++){

        int win_freq[26]={0};
        int win_idx=0,idx=i;

        while(win_idx<n1 && idx<n2){
            win_freq[s2[idx]-'a']++;
            win_idx++;idx++;
        }

        if(isFreqSame(win_freq,freq)) return true;

    }

    return false;
}