class Node:
    def __init__(self, data):
        self.data=data
        self.nref=None
        self.pref=None
class doublylinkedlist:
        def __init__(self):
            self.head=None
        def Print_LL(self):
            if self.head is None:
                print("linked list is empty")
            else:
                n=self.head
                while n is not None:
                    print(n.data,"-->",end=" ")
                    n=n.nref
        def Print_LL_reverse(self):
            if self.head is None:
                print("linked list is empty")
            else:
                n=self.head
                while n.nref is not None:
                    n=n.nref
                while n is not None:
                    print(n.data,"-->",end="")
                    n=n.pref
ll1=doublylinkedlist()
ll1.Print_LL()
ll1.Print_LL_reverse()
                
    
        

