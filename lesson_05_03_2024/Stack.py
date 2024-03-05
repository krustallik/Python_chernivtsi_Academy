class Stack:
    def __init__(self, list=None):
        if list is None:
            list = []
        self.stack = list

    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()  # deleting the last one element
        else:
            print("Stack is empty")

    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]  # return last element
        else:
            return "Stack is empty"

    def push(self, item):
        self.stack.append(item)  # add new element to the end of stack

    def is_empty(self):
        return len(self.stack) == 0 #true if is empty

    def size(self):
        return len(self.stack) #return size

# creating stack
my_stack = Stack()

# condition if stack is empty
print("Is the stack empty?", my_stack.is_empty())

# adding numbers to the stack
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

# checking size of stack after adding elements
print("Stack size after pushing elements:", my_stack.size())  # Виведе: 3

# getting top element of stack
print("Top element of the stack:", my_stack.top())  # Виведе: 3

# deleting top element
my_stack.pop()

# getting top element of stack after pop funktion
print("Top element of the stack after popping:", my_stack.top())  # Виведе: 2

# checking size after deleting
print("Stack size after popping an element:", my_stack.size())  # Виведе: 2

# checking if stzck is empty after double pop
my_stack.pop()
my_stack.pop()
print("Is the stack empty after popping all elements?", my_stack.is_empty())

# trying to delete element from empty stack
my_stack.pop()
