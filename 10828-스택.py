a = int(input())

list = []
stack = []

def pop():
    if (len(stack) == 0):
        print("-1")
    else:
        print(stack.pop())

def size():
    print(len(stack))

def empty():
    if (len(stack) == 0):
        print("1")
    else:
        print("0")

def top():
    if (len(stack) == 0):
        print("-1")
    else:
        print(stack[len(stack) - 1])

for i in range(a):
    list.append(input())
for j in list:
    if (j[0:3] == "pus"):
        stack.append(j[5:])
    elif (j == "pop"):
        pop()
    elif (j == "empty"):
        empty()
    elif (j == "size"):
        size()
    else:
        top()