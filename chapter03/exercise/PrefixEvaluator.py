from structures.stack import Stack


def calculate(op, operand_one, operand_two):
    result = ''
    if op == '+':
        result = operand_one + operand_two
    elif op == '-':
        result = operand_one - operand_two
    elif op == '*':
        result = operand_one * operand_two
    elif op == '/':
        result = operand_one / operand_two
    elif op == '**':
        result = operand_one ** operand_two

    return result


def evaluate_prefix_expr(infix_expr):
    ops = '(+-*/**)'
    operands = Stack()
    list_expr = infix_expr.split(' ')
    list_expr.reverse()
    for token in list_expr:
        if token in ops:
            operand_one = operands.pop()
            operand_two = operands.pop()
            operands.push(calculate(token, int(operand_one), int(operand_two)))
        else:
            operands.push(token)

    return operands.pop()


print(evaluate_prefix_expr('+ 8 2'))
print(evaluate_prefix_expr('* 8 2'))
print(evaluate_prefix_expr('+ 8 * 2 10'))
print(evaluate_prefix_expr('* 8 + 2 10'))
