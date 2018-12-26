from structures.stack import Stack


def convert_infix_to_prefix(expression):
    prefix_expr = Stack()
    ops = '+-*/'
    expr_list = list(expression)

    for token in expr_list:
        if token == '(':
