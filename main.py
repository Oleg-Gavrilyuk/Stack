from pythonds.basic.stack import Stack

class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def pop(self):
        removed = self.stack.pop()
        return removed

    def push(self, item):
        self.stack.append(item)

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    symbols = ['(', '[', '{']
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in symbols:
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


def checkParenth(str):
    stack = Stack()
    pushChars, popChars = "<({[", ">)}]"
    for c in str:
        if c in pushChars:
            stack.push(c)
        elif c in popChars:
            if stack.isEmpty():
                return False
            else:
                stackTop = stack.pop()
                balancingBracket = pushChars[popChars.index(c)]
                if stackTop != balancingBracket:
                    return False
        else:
            return False

    return stack.isEmpty()


if __name__ == "__main__":
    # stack = Stack()
    # stack.push(1)
    # stack.pop()
    # stack.push(2)
    # stack.peek()
    print(checkParenth('(((([{}]))))'))
    print(checkParenth('[([])((([[[]]])))]{()}'))
    print(checkParenth('{{[()]}}'))
    print(checkParenth('{{}{'))
    print(checkParenth('{{[(])]}}'))
    print(checkParenth('[[{())}]'))
