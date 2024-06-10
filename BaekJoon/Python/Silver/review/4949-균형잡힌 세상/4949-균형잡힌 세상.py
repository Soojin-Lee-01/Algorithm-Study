while True:
    data = input()
    if data == '.':
        break
    else:
        check = 0
        stack = []
        for i in range(len(data)):
            if data[i] == '(':
                stack.append('(')
            elif data[i] == '[':
                stack.append('[')
            elif data[i] == ')':
                if len(stack) > 0:
                    if stack[len(stack)-1] == '(':
                        stack.pop()
                    else:
                        check = 1
                else:
                    check = 1
            elif data[i] == ']':
                if len(stack) > 0:
                    if stack[len(stack)-1] == '[':
                        stack.pop()
                    else:
                        check = 1
                else:
                    check = 1

    if check == 0 and len(stack) == 0:
        print("yes")
        stack.clear()
    else:
        print("no")