class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def print_list(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next

    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def append(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while(last.next):
            last=last.next 
        last.next=new_node
    def insert_after(self,prev_node,new_data):
        if prev_node is None:
            print("it should not be none")
            return
        new_node=Node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node 
    def delete_by_value(self,key):
        temp=self.head
        if self.head and self.head.data==key:
            self.head=self.head.next
            temp=None
            return self.head
        prev=None
        while(temp.next is not None and temp.data!=key):
            prev=temp
            temp=temp.next  
        if (temp.next is None and temp.data!=key):
            print("there is no such element present in this linked list")
        elif (temp.next is None and temp.data==key):
            prev.next=None
        else:
            prev.next=temp.next        
        
               
if __name__ == "__main__":
    llist=LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(4)
    llist.append(5) 
    llist.insert_after(llist.head.next.next,13)

    llist.delete_by_value(13)
    llist.print_list()            
