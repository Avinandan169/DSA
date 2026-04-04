void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    int i=0,j=0,k=0,temp[m+n];
    while(i<m && j<n){
        if(nums1[i]<=nums2[j]){
            temp[k++]=nums1[i++];
        }else{ 
            temp[k++]=nums2[j++];
        }
    }
    if(i==m){
        while(j<n){
            temp[k++]=nums2[j++];
        }
    }else{ 
        while(i<m){
            temp[k++]=nums1[i++];
        }
    }
    for(i=0;i<k;i++){
        nums1[i]=temp[i];
    }
}