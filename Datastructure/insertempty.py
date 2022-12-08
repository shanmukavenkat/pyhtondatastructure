class Node:
    def __init__(self, data):
        self.data=data
        self.ref=None
class Linkedlist:
    def __init__(self):
            self.head=None
    def Print_LL(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
    def insert_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("linked list is not empty")
LL1=Linkedlist()
LL1.insert_empty(10)
LL1.Print_LL()
