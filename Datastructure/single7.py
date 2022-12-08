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
    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        if n is None:
            print("node is not present in linked list")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
    def add_before(self,data,x):
        if self.head is None:
            print("liknked list is empty")
            return
        if self.head.data==x:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
            return
        n=self.head
        while n.ref is not None:
           if n.ref.data==x:
               break
           n=n.ref
        if n.ref is None:
           print("Node is not present")
        else:
           new_node=Node(data)
           new_node.ref=n.ref
           n.ref=new_node
LL1=Linkedlist()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin(30)
LL1.add_begin(40)
LL1.add_before(50,20)
LL1.Print_LL()



