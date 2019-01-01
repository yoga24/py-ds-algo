from structures.stack import Stack

precedence = {
    '(': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '**': 3,
    ')': 0,
}

ops = '(+-*/)'


def convert_infix_to_postfix(infix_expr):
    op = Stack()
    postfix = []
    infix = list(infix_expr)
    for index in range(len(infix)):
        if infix[index] in ops:
            while (not op.is_empty()) and precedence[op.peek()] >= precedence[infix[index]]:
                if op.peek() == '(':
                    op.pop()
                else:
                    postfix.append(op.pop())
            if infix[index] != ')':
                op.push(infix[index])
        elif infix[index] != ' ':
            postfix.append(infix[index])

    while op.size() > 0:
        postfix.append(op.pop())

    print(''.join(postfix))


def convert_infix_to_postfix_new(infix_expr):
    op = Stack()
    postfix = []
    infix = list(infix_expr)
    for index in range(len(infix)):
        token = infix[index]
        if token not in ops:
            postfix.append(token)
        elif token == '(':
            op.push(token)
        elif token == ')':
            while op.peek() != '(':
                postfix.append(op.pop())
            op.pop()
        else:
            while (not op.is_empty()) and precedence[op.peek()] >= precedence[infix[index]]:
                postfix.append(op.pop())
            op.push(token)

    while not op.is_empty():
        postfix.append(op.pop())

    print(''.join(postfix))


# convert_infix_to_postfix('(a+b)')
convert_infix_to_postfix('( A + B ) * ( C + D )')
convert_infix_to_postfix_new('( A + B ) * ( C + D )')
# convert_infix_to_postfix('( A + B ) * C')
# convert_infix_to_postfix('a+b*c')
# convert_infix_to_postfix("A * B + C * D")
# convert_infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )")
