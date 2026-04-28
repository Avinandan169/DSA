/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    if(head==NULL || head->next==NULL){
        return head;
    }

    struct ListNode start;
    start.next=head;
    struct ListNode* prev=&start;

    while(head!=NULL){
        if(head->next!=NULL && head->next->val==head->val){
            while(head->next!=NULL && head->next->val==head->val){
                struct ListNode* temp=head;
                head=head->next;
                free(temp);
            }
            prev->next=head->next;
            free(head);
        }else{
            prev=prev->next;
        }
        head=prev->next;
    }

    return start.next;
}
    
    
    