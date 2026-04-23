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

void traverse(struct TreeNode *root,int* arr,int* index){
    if (root==NULL) return;
    traverse(root->left,arr,index);
    arr[(*index)++] = root->val;
    traverse(root->right,arr,index);
}

int* inorderTraversal(struct TreeNode* root, int* returnSize) {
    *returnSize=count(root);
    if(*returnSize==0) return NULL;
    int* result=(int*)malloc(*returnSize * sizeof(int));
    int index=0;
    traverse(root,result,&index);
    return result;
}