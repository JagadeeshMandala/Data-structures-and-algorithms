class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None

if __name__=="__main__":
    llist=Linkedlist()
    llist.head=Node(1)
    second=Node(2)  
    third=Node(3)
    llist.head.next=second;
    second.next=third;                  