class Node:
    data:str


    def __init__(self,data,next=None):
        self.data=data
        self.next=None
        self.prev=None

class Double_Ended_Queue():

    def __init__(self):
        self.head_left=None
        self.head_right=None
    
    def push_left(self,data):
        new_node=Node(data)
        if self.head_left is None:
            self.head_left=new_node
            self.head_right=new_node
        else:
            new_node.next=self.head_left
            self.head_left.prev=new_node
            self.head_left=new_node
    
    def push_right(self,data):
        new_node=Node(data)
        if self.head_right is None:
            self.head_left=new_node
            self.head_right=new_node
        else:
            new_node.prev=self.head_right
            self.head_right.next=new_node
            self.head_right=new_node
    
    def pop_left(self):
        print("pop left")
        if self.head_left is None:
            return None
        eliminated_data=self.head_left.data

        
        if self.head_left==self.head_right:
            self.head_left=None
            self.head_right=None
        else:
            self.head_left=self.head_left.next
            self.head_left.prev=None
        
        return eliminated_data
    
    def pop_right(self):
        print("pop right")
        if self.head_right is None:
            return None
        
        eliminated_data=self.head_right.data

        if self.head_left==self.head_right:
            self.head_left=None
            self.head_right=None
        else:
            self.head_right=self.head_right.prev
            self.head_right.next=None
        
        return eliminated_data

    def print_structure(self):
        if self.head_left is None:
            print("Estructura vacía")
            print("*"*20)
            return
        current=self.head_left
        output=[]
        while current is not None:
            output.append(str(current.data))
            current=current.next
        print(output)
        print("*"*20)

#Main
my_deq=Double_Ended_Queue()

my_deq.push_left("Node A")
my_deq.push_right("Node B")
my_deq.push_left("initial Node")
my_deq.push_right("final Node")

my_deq.print_structure()

my_deq.pop_left()
my_deq.print_structure()

my_deq.pop_right()
my_deq.print_structure()


