class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed

    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)


sam_stack = Stack()


def sam_stack_push():
    for i in range(10):
        sam_stack.push(i)


print(f'Current stack: {sam_stack.stack}')
print(f'Is stack empty?: {sam_stack.is_empty()}')
print(f'Pushing items to stack: {sam_stack_push()}')
print(f'Popped item: {sam_stack.pop()}')
print(f'Check item on top: {sam_stack.peek()}')
print(f'Check stack size: {sam_stack.size()}')
print(f'Current stack: {sam_stack.stack}')
print(f'Is stack empty?: {sam_stack.is_empty()}')


def balanced_brackets(incoming_brackets):
    bracket_stack = Stack()
    possible_brackets = {'(': ')', '{': '}', '[': ']'}
    for bracket in incoming_brackets:
        if bracket in ['(', '{', '[']:
            bracket_stack.push(bracket)
        else:
            if not bracket_stack.is_empty():
                top = bracket_stack.pop()
                if possible_brackets[top] != bracket:
                    return False
            else:
                return False
    return False if not bracket_stack.is_empty() else True


b_brackets = '[([])((([[[]]])))]{()}'
n_b_brackets = '[[{())}]'

print(f'Are brackets {b_brackets} balanced?: {balanced_brackets(b_brackets)}')
print(f'Are brackets {n_b_brackets} balanced?: {balanced_brackets(n_b_brackets)}')
