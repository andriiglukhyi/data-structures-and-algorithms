from stack import Stack


def moveTower(init_stack, buffer_stack, final_stack, number):
    if number == 0:
        return
    elif number == 1:
        final_stack.push(init_stack.pop())
    elif number == 2:
        buffer_stack.push(init_stack.pop())
        final_stack.push(init_stack.pop())
        final_stack.push(buffer_stack.pop())
    else:
        print(number)
        moveTower(init_stack, final_stack, buffer_stack, number-1)
        final_stack.push(init_stack.pop())
        moveTower(buffer_stack, init_stack, final_stack, number-1)


def towers_of_hanoi(number):
    if number > 0 and type(number) is int:
        init_stack = Stack()
        buffer_stack = Stack()
        final_stack = Stack()
        for item in range(1, number+1):
            buffer_stack.push(item)
        for _ in range(len(buffer_stack)):
            init_stack.push(buffer_stack.pop())
        
        moveTower(init_stack, buffer_stack, final_stack, number)
        # import pdb; pdb.set_trace()
        return final_stack

    else:
        return False

