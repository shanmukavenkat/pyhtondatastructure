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
                print(n.data,"---->",end="")
                n=n.ref
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def delete_begin(self):
        if self.head is None:
            print("ll is empty so we cant delete nodes")
        else:
            self.head=self.head.ref
LL1=Linkedlist()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin(30)
LL1.add_begin(40)
LL1.delete_begin()
LL1.Print_LL()
