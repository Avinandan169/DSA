/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    if(list1==NULL) return list2;
    if(list2==NULL) return list1;
    struct ListNode *l1=list1, *l2=list2, dummy;
    struct ListNode* tail;
    tail=&dummy;
    dummy.next=NULL;
    while(l1!=NULL && l2!=NULL){
        if(l1->val<=l2->val){
            tail->next=l1;
            l1=l1->next;
        }else{
            tail->next=l2;
            l2=l2->next;
        }  
        tail=tail->next;  
    }
    if(l1!=NULL) tail->next=l1;
    else tail->next=l2;
    return dummy.next;
}