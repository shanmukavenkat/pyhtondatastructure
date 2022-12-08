class TNode:
    def __init__(self, key):
        self.left = None
        self.data = key
        self.right = None
        
class searchTree:
    def __init__(self):
        self.root = None
        self.parent = None
        
    def insertNode(self, ptr, newNode):
        if(ptr==None):
            self.root = newNode
        elif(newNode.data < ptr.data):
            if(ptr.left == None):
                ptr.left = newNode
            else:   
                self.insertNode(ptr.left, newNode)
                
        elif(newNode.data >= ptr.data):
            if(ptr.right == None):
                ptr.right = newNode
            else:
                self.insertNode(ptr.right, newNode)     
    
    def createTree(self):
        n = int(input("\nNumber of nodes\n"))
        for i in range(n):
            ele = int(input("Enter data\n"))
            newNode = TNode(ele)
            print("\nNode is created")
            if(newNode!=None):
                self.insertNode(self.root, newNode)
                print("Node is inserted\n")
            
            else:
                print("\nInsufficient Memory!!!\n")
                
    def deleteNode(self, ptr, key):
        if(ptr==None):
            print("Key is not found")
        elif(key<ptr.data):
            self.parent = ptr
            self.deleteNode(ptr.left, key)
        elif(key>ptr.data):
            self.parent = ptr
            self.deleteNode(ptr.right, key)
        elif(key==ptr.data):
            if(ptr.left!=None and ptr.right!=None):
                dup = self.inOrderSuccessor(ptr)
                ptr.data = dup
                self.deleteNode(ptr.right, dup)
            else:
                temp = ptr
                if(self.parent.left==ptr):
                    if(ptr.left==None):
                        self.parent.left = ptr.right
                        ptr.right = None
                    elif(ptr.right==None):
                        self.parent.left=Ptr.left
                        ptr.left = None
                elif(self.parent.right==ptr):
                    if(ptr.left==None):
                        self.parent.right = ptr.right
                        ptr.right = None
                    elif(ptr.right==None):
                        self.parent.right = ptr.left
                        ptr.left = None
        
    def inOrder(self, ptr):                
        if(ptr!=None):
            self.inOrder(ptr.left)
            print(ptr.data, end = " ")
            self.inOrder(ptr.right)
            
    def preOrder(self, ptr):                
        if(ptr!=None):
            print(ptr.data, end = " ")
            self.preOrder(ptr.left)
            self.preOrder(ptr.right)
            
    def postOrder(self, ptr):                
        if(ptr!=None):
            self.postOrder(ptr.left)
            self.postOrder(ptr.right)
            print(ptr.data, end = " ")
     
    def inOrder_Desc(self, ptr):
        if(ptr!=None):
            self.inOrder_Desc(ptr.right)
            print(ptr.data, end = " ")
            self.inOrder_Desc(ptr.left)
    
    def findMinimum(self, ptr):
        if(ptr.left == None):
            min = ptr.data
        else:
            while(ptr.left!=None):
                ptr = ptr.left
            min = ptr.data
        return min
    
    def findMaximum(self, ptr):
        if(ptr.right==None):
            max = ptr.data
        else:
            while(ptr.right!=None):
                ptr = ptr.right
            max = ptr.data
        return max
        
    def searchNode(self, ptr, key):
        if(ptr==None):
            print("\nKey is not found")
        elif(key==ptr.data):
            print("\nKey is found")
    
        elif(key< ptr.data):
            self.searchNode(ptr.left, key)
            
        elif(key>ptr.data):
            self.searchNode(ptr.right, key)
            
    def inOrderPredecessor(self, ptr):
        if(ptr.left==None):
            ip = ptr.data
        else:
            ptr = ptr.left
            ip = self.findMaximum(ptr)
        return ip

    def inOrderSuccessor(self, ptr):
        if(ptr.right==None):
            iss = ptr.data
        else:
            ptr = ptr.right
            iss = self.findMinimum(ptr)
        return iss
    
s = searchTree()
s.createTree()
print("Tree is")
s.inOrder(s.root)
while(True):
    print("\n\n1. Insert node\n2. Delete node\n3. Search node")
    print("4. Inorder(asc)\n5. Inorder(desc)\n6. Preorder")
    print("7. Postorder\n8. Display minimum\n9. Display maximum")
    print("10. Inorder successor\n11. Inorder predecessor")
    op = int(input("\nSelect the option\n"))
    if(op==1):
        ele = int(input("Enter Data\n"))
        newNode = TNode(ele)
        s.insertNode(s.root, newNode)
        print("Tree is")
        s.inOrder(s.root)
    else:
        if(s.root!=None):
            if(op==2):
                ele = int(input("Enter data to delete\n"))
                s.deleteNode(s.root, ele)
                print("Tree is")
                s.inOrder(s.root)
            elif(op==3):
                ele = int(input("Enter data to search\n"))
                s.searchNode(s.root, ele)
            elif(op==4):
                print("\nInorder (Asc order) is")
                s.inOrder(s.root)
            elif(op==5):
                print("\nInorder (Desc order) is")
                s.inOrder_Desc(s.root)
            elif(op==6):
                print("\nPreorder is")
                s.preOrder(s.root)
            elif(op==7):
                print("\nPostorder is")
                s.postOrder(s.root)
            elif(op==8):
                print("\nMinimum is %d" % s.findMinimum(s.root))
            elif(op==9):
                print("\nMaximum is %d" % s.findMaximum(s.root))
            elif(op==10):
                print("\nInorder successor is %d" % s.inOrderSuccessor(s.root))
            elif(op==11):
                print("\nInorder predecessor is %d" % s.inOrderPredecessor(s.root))
            else:
                exit()
        else:
            print("Tree is empty\n")
    
    