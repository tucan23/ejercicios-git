class Node:
    
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def adding(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        actual=self.head
        #print(actual.next)
        while actual.next:
            actual=actual.next
        actual.next=new_node
        
    
    def bubble_sort(self):
        swapped=True
        while swapped:
            swapped=False
            actual=self.head
            
            #print(actual.next)
            while actual.next is not None:
                next_node=actual.next
                if actual.data>next_node.data:
                    actual.data, next_node.data = next_node.data, actual.data
                    #print(swapped,actual.data,next_node)
                    swapped=True
                actual=actual.next
        
    def print_structure(self):
        actual=self.head
        elements=[]
        while actual:
            elements.append(actual.data)
            actual=actual.next
        print(elements)

#main
list1=LinkedList()

list1.adding(5)
list1.adding(4)
list1.adding(8)
list1.adding(1)

list1.print_structure()

list1.bubble_sort()

list1.print_structure()
