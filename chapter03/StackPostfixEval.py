from structures.stack import Stack


def evaluate_postfix_expr(post_expr):
    expr = post_expr.split(' ')
    operands = Stack()
    ops = '+-/*'

    for token in expr:
        if token not in ops:
            operands.push(token)
        else:
            second_operand = operands.pop()
            first_operand = operands.pop()
            result = 0
            if token == '+':
                result = int(first_operand) + int(second_operand)
            elif token == '-':
                result = int(first_operand) - int(second_operand)
            elif token == '*':
                result = int(first_operand) * int(second_operand)
            elif token == '/':
                result = int(first_operand) / int(second_operand)
            operands.push(result)

    print(operands.pop())


evaluate_postfix_expr('17 10 + 3 * 9 /')


