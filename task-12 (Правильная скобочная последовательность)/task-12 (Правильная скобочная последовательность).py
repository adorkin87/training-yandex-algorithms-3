class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()
        else:
            print('error')

    def back(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            print('error')

    def size(self):
        return len(self.stack)


line = input()
stack = Stack()
close_brackets = {')', ']', '}'}
open_brackets = {'(', '[', '{'}
if line == '':
    print('yes')
else:
    for bracket in line:
        if stack.size() == 0 and bracket in close_brackets:
            print('no')
            break
        elif bracket in open_brackets:
            stack.push(bracket)
        else:
            if (bracket == ')' and stack.back() == '(')\
                    or (bracket == ']' and stack.back() == '[')\
                    or (bracket == '}' and stack.back() == '{'):
                stack.pop()
            else:
                print('no')
                break
    else:
        print('yes') if stack.size() == 0 else print('no')
