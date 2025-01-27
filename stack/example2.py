from stack import Stack

def is_balanced_p(expression):
    stack = Stack()
    opening = "({["
    closing = ")}]"


    pairs = dict(zip(closing, opening))
    print(pairs)


    for char in expression:
        if char in opening:
            stack.push(char)

        elif char in closing:    
            if stack.is_empty():
                return False
            
            var = stack.pop()
            print(var)

            if  var != pairs[char]:
                return False
            
        print(stack)

        return stack.is_empty()   
    

print(is_balanced_p("()"))    



