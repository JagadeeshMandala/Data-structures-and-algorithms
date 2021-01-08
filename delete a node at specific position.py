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
            print(temp.data,end=' ')
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
    def list_length(self):
        temp=self.head
        length=0
        while(temp):
            length+=1
            temp=temp.next
            
        return length
    def delete_at_position(self,position):
        if position<0 or position>self.list_length():
            print("invalid position is given")
        temp=self.head
        if position==0:
            self.head=temp.next
            temp=None
            return

        for i in range(position-1):
            temp=temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return    
        next=temp.next.next
        temp.next=None
        temp.next=next          
        
        

if __name__ == "__main__":
    
    llist=LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(4)
    llist.push(6)
    llist.push(3)
    llist.append(5) 
    llist.insert_after(llist.head.next.next,9)
    print("the length of the list is",llist.list_length())
    #llist.delete_at_position(3)
    llist.print_list()            
