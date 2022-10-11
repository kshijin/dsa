from dynamic import Stack

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print ("Top element is % d " % (stack.peek()))
    print ("% d popped from stack" % (stack.pop()))
    print ("Top element is % d " % (stack.peek()))