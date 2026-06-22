

typedef struct {
    int q1[200];
    int q2[200];
    int f1,r1;
    int f2,r2;
} MyStack;


MyStack* myStackCreate() {
    MyStack* stack=(MyStack*)malloc(sizeof(MyStack));
    stack->f1=0;stack->f2=0;
    stack->r1=0;stack->r2=0;
    return stack;
}

void myStackPush(MyStack* obj, int x) {
    obj->q2[obj->r2++]=x;

    while(obj->f1<obj->r1){
        obj->q2[obj->r2++]=obj->q1[obj->f1++];
    }
    int idx=0;
    while(obj->f2<obj->r2){
        obj->q1[idx++]=obj->q2[obj->f2++];
    }
    obj->f2=0;
    obj->r2=0;
    obj->f1=0;
    obj->r1=idx;
}

int myStackPop(MyStack* obj) {
    return obj->q1[obj->f1++];
}

int myStackTop(MyStack* obj) {
    return obj->q1[obj->f1];
}

bool myStackEmpty(MyStack* obj) {
    return obj->f1==obj->r1;
}

void myStackFree(MyStack* obj) {
    free(obj);
}

/**
 * Your MyStack struct will be instantiated and called as such:
 * MyStack* obj = myStackCreate();
 * myStackPush(obj, x);
 
 * int param_2 = myStackPop(obj);
 
 * int param_3 = myStackTop(obj);
 
 * bool param_4 = myStackEmpty(obj);
 
 * myStackFree(obj);
*/