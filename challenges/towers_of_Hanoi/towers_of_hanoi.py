from stack import Stack

def towers_of_hanoi(number):
    # import pdb; pdb.set_trace()
    if number > 0 and type(number) is int:
        init_stack = Stack()
        buffer_stack = Stack()
        final_stack = Stack()
        for item in range(1, number+1):
            buffer_stack.push(item)
        init_stack.push(buffer_stack.pop())

        def moveTower(init_stack, buffer_stack, final_stack):
            if init_stack.top is None:
                print(str(final_stack))
                return final_stack
            elif init_stack._next is None:
                print(str(final_stack))
                final_stack.push(init_stack.pop())
            elif final_stack._next is not None:
                print(str(final_stack))
                moveTower(init_stack, final_stack, buffer_stack)
                final_stack.push(init_stack.pop())
                moveTower(buffer_stack, init_stack, final_stack)
        return final_stack

    else:
        return False
    

if __name__ == '__main__':
    towers_of_hanoi(5)