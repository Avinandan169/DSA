/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdlib.h>

int* nextGreaterElement(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    int* stack=(int*)malloc(nums2Size*sizeof(int));
    int top=-1;

    int next_greater[10001];
    for (int i=0;i<10001;i++) {
        next_greater[i]=-1;
    }

    for(int i=0;i<nums2Size;i++) {
        int num=nums2[i];
        while(top!=-1 &&num>stack[top]) {
            int popped_num=stack[top--];
            next_greater[popped_num]=num;
        }
        stack[++top]=num;
    }

    int* ans=(int*)malloc(nums1Size*sizeof(int));
    for (int i=0;i<nums1Size;i++) {
        ans[i]=next_greater[nums1[i]];
    }

    free(stack);
    *returnSize=nums1Size;
    return ans;
}