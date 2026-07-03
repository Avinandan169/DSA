void setZeroes(int** matrix, int matrixSize, int* matrixColSize) {
    int m=matrixSize;
    int n=matrixColSize[0];
    bool firstrow=false;
    bool firstcol=false;

    for(int i=0;i<n;i++){
        if(matrix[0][i]==0){
            firstrow=true;
        }
    }
    for(int i=0;i<m;i++){
        if(matrix[i][0]==0){
            firstcol=true;
        }
    }

    for(int i=1;i<m;i++){
        for(int j=1;j<n;j++){
            if(matrix[i][j]==0){
                matrix[i][0]=0;
                matrix[0][j]=0;
            }
        }
    }
    for(int i=1;i<m;i++){
        for(int j=1;j<n;j++){
            if(matrix[i][0]==0 || matrix[0][j]==0){
                matrix[i][j]=0;
            }
        }
    }
    if(firstrow){
        for(int i=0;i<n;i++){
            matrix[0][i]=0;
        }
    }
    if(firstcol){
        for(int i=0;i<m;i++){
            matrix[i][0]=0;
        }
    }
}