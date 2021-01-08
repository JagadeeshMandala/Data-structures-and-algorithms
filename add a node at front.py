class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        new_node.next=self.head
        self.head=new_node
    def print_list(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
if __name__ == "__main__":
    ll=LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(5)
    ll.print_list()
