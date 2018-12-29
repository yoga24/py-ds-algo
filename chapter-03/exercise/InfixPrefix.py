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


def reverse_string(string):
    reverse_str = []
    for index in range(len(string) - 1, -1, -1):
        reverse_str.append(string[index])
    return ''.join(reverse_str)


def convert_infix_to_prefix(infix_expression):
    reverse = reverse_string(infix_expression)
    operators = Stack()
    prefix_expr = []
    ops = '(+-*/**)'
    expr_list = list(reverse)

    for token in expr_list:
        if token not in ops:
            prefix_expr.append(token)
        elif token == ')':
            operators.push(token)
        elif token == '(':
            while operators.peek() != ')':
                prefix_expr.append(operators.pop())
            operators.pop()
        else:
            while (not operators.is_empty()) and precedence[operators.peek()] > precedence[token]:
                prefix_expr.append(operators.pop())
            operators.push(token)

    while not operators.is_empty():
        prefix_expr.append(operators.pop())

    return reverse_string(''.join(prefix_expr))


print(convert_infix_to_prefix('(A+B)'))
print(convert_infix_to_prefix('A+B*C'))
