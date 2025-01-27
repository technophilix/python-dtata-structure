class Stack:
    def __init__(self):
        self.items = []


    def is_empty(self):
        return len(self.items)==0
    

    def length(self):

        return len(self.items)


    def push(self, item):
        self.items.append(item)


    def pop(self):
        if not self.is_empty():
            return self.items.pop()

        raise IndexError("Stack is not empty")


    def peek(self):
        if not self.is_empty():
            return self.items[-1]

        raise IndexError("Stack is not empty")
    

    def __str__(self):
        return str(self.items)

    

            