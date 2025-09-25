# codes for challenge

#Step 1:
#define the stack
stack = []
#Step 2 push element in stack
stack.append("X")
stack.append("Y")
stack.append("Z")
stack.append("W")
#Step 3: pop all
#we can use for loop or just pop step by step using step by step
stack.pop()
stack.pop()
stack.pop()
print("Stack after popping 3 elements", stack[-1]) #top of stack

#the top of stack is "W"