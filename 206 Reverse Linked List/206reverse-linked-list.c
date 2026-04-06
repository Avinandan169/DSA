/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* prev=NULL,*curr=head,*ahead=NULL;
    
    while(curr!=NULL){
        ahead=curr->next;
        curr->next=prev;
        prev=curr;
        curr=ahead;
    }
    return prev;
}