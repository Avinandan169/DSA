int max(int a,int b){
    return (a>b) ? a : b; 
}
int longestCommonSubsequence(char* text1, char* text2) {
    int m=strlen(text1);
    int n=strlen(text2);

    int L[m+1][n+1];

    for(int i=0;i<=m;i++){
        for(int j=0;j<=n;j++){
            if(i==0 || j==0){
                L[i][j]=0;
            }else if(text1[i-1]==text2[j-1]){
                L[i][j]=L[i-1][j-1]+1;
            }else{
                L[i][j]=max(L[i-1][j],L[i][j-1]);
            }
        }
    }
    return L[m][n];
}