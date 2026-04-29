/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int count(struct TreeNode* root){
    if(root==NULL) return 0;
    return 1 + count(root->left) + count(root->right);
}
void traverse(struct TreeNode* root,int* arr,int* index){
    if(root==NULL) return;
    arr[(*index)++]=root->val;
    traverse(root->left,arr,index);
    traverse(root->right,arr,index);
}
int* preorderTraversal(struct TreeNode* root, int* returnSize) {
    *returnSize=count(root);
    if(*returnSize==0) return NULL;
    int index=0;
    int* result=(int*)malloc(*returnSize*sizeof(int));
    traverse(root,result,&index);
    return result;
}
