class Stack:
    def __init__(self):
        self.stack = []

    def push(self, bracket):
        self.stack.append(bracket)

    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()
        else:
            print('error')

    def back(self):
        if len(self.stack) > 0:
            return (self.stack[-1])
        else:
            print('error')

    def size(self):
        return len(self.stack)


str = input()
stack = Stack()
close_brackets = {')', ']', '}'}
open_brackets = {'(', '[', '{'}
if str == '':
    print('yes')
else:
    for bracket in str:
        if stack.size() == 0 and bracket in close_brackets:
            print('no')
            break
        elif bracket in open_brackets:
            stack.push(bracket)
        else:
            if (bracket == ')' and stack.back() == '(') or (bracket == ']' and stack.back() == '[') or (bracket == '}' and stack.back() == '{'):
                stack.pop()
            else:
                print('no')
                break
    else:
        if stack.size() == 0:
            print('yes')
        else:
            print('no')