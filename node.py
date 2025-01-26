class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None 

    def insertAtBegin(self, data):
        new_node = Node(data)
        new_node.next= self.head
        self.head = new_node

    def is_empty(self):
        return self.head is None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return


        current = self.head
        while current.next:
            current= current.next
        current.next = new_node


    def insertAtIndex(self, data, index):

        if index< 0:
            print("Not possible")

        if index == 0:
            self.insertAtBegin(data)
            return
        

        new_node = Node(data)
        current_node= self.head
        position = 0
        
        while current_node and position < index-1:
            position += 1
            current_node = current_node.next   

        if current_node is None:
            print("Index out od bound")

        new_node.next = current_node.next
        current_node.next=new_node    
          

    def show_linked(self):
        current = self.head
        while current:
            print(current.data, end="->")    
            current = current.next
        print("NULL")   

    def insert_after(self, prev_node_value, data):

        prev_node = self.get_node(prev_node_value)
        if prev_node is None:
            print("Previous node is not found")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next= new_node    

    def get_node(self, value):
        current = self.head
        while current:
            if current.data==value:
                return current
            current= current.next
        return None    
    
    def delete_node(self, value):
        current = self.head

        # if head node is the value
        if current and current.data == value:
            self.head = current.next
            return
        
        while current and current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next

    def delete_at_position(self, position):
        if self.head is None:
            return
        if position == 0:
            self.head = self.head.next
            return
        
        current = self.head

        for i in range(position-1):
            if current is None:
                return
            current = current.next

        if current is None or current.next is None:
            return

        current.next = current.next.next    


    def search(self, value):
        position = 0
        current = self.head

        while current:
            if current.data == value:
                return position
            current = current.next
            position = position+1

        return -1        







if __name__== "__main__":
    llist = Linkedlist()
    llist.insertAtBegin(1)
    llist.show_linked()

    llist.insertAtIndex(4,1)
    llist.show_linked()
    llist.insert_at_end(36)
    llist.show_linked()

    llist.insert_after(4,89)
    llist.show_linked()
    llist.delete_node(1)
    llist.show_linked()
    llist.delete_node(36)
    llist.show_linked()



