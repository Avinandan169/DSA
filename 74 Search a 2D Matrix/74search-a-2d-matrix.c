bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target) {
    int m=matrixSize;
    int n=matrixColSize[0];
    int low=0;
    int high=(m*n)-1;
    int r,c,mid;
    while(low<=high){
        mid=low+(high-low)/2;
        r=mid/n;
        c=mid%n;
        if(matrix[r][c]==target){
            return true;
        }else if(matrix[r][c]<target){
            low=mid+1;
        }else{
            high=mid-1;
        }
    }
    return false;
}
