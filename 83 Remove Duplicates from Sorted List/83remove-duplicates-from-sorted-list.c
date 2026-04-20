/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    struct ListNode* curr=head;
    struct ListNode* delete;
    while(curr!=NULL && curr->next!=NULL){
        if(curr->val==curr->next->val){
            delete=curr->next;
            curr->next=curr->next->next;
            free(delete);
        }else{
            curr=curr->next;
        }
    }
    return head;
}