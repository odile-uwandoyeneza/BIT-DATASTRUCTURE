from collections import deque
print("Stack Questions: \n Practical (Rwanda): UR pushes ")
ur = []
ur.append("LectureA")
ur.append("LectureB")
ur.append("LectureC")
print("Ur pushes:",ur)
ur.pop()
print("Ur pushes after pop:",ur)
print('Ur push top is equal to: ', 'none' if len(ur)== 0 else ur[-1])


print("Irembo Stack Questions:")
irembo = []
irembo.append("upload")
irembo.append("fill")
irembo.append("confirm")
print("Irembo pushes:",irembo)
irembo.pop()
irembo.pop()
print("irembo after undo 2:",irembo)


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

print("Reflection: Why stack is efficient for backtracking?")
print("Becouse You can turn back whenever you make a mistake, and use memory efficiently")

print("Queue Questions:")
print("Practical Airtel:")
aitel = deque()
aitel.append("client 1")
aitel.append("client 2")
aitel.append("client 3")
aitel.append("client 4")
aitel.append("client 5")
aitel.append("client 6")
aitel.append("client 7")

print('AITEL queue', aitel)
print('Client 1 was served', aitel.popleft())
print('Client 2 was served', aitel.popleft())
print('Client 3 was served', aitel.popleft())
print('Client 4 was served', aitel.popleft())
print("Front  Client is ", aitel[0])

print("At BK ATM, 10 clients queue. Who is last?")
chuk = deque()
chuk.append("patient 1")
chuk.append("patient 2")
chuk.append("patient 3")
chuk.append("patient 4")
chuk.append("patient 5")
chuk.append("patient 6")
print("Last patient is:", chuk[-1])

print("Challenge: Queue vs stack for food queue in cafeteria. Which works?")
print("Answer: Queue becouse who booked first will be served first")
print("Reflection: Why FIFO promotes fairness in dining halls?")
print("Becouse everyone will be served in order they came")



