from structures.BinaryTree import BinaryTree
from structures.stack import Stack


def construct_parse_tree(expression):
    operators = ['(', ')', '+', '-', '*', '/']
    # expr_list = expression.split()
    parse_tree = BinaryTree(None)
    current_tree = parse_tree
    path = Stack()
    path.push(parse_tree)
    for token in expression:
        if token == '(':
            current_tree.insert_left(' ')
            path.push(current_tree)
            current_tree = current_tree.get_left()
        elif token not in operators:
            try:
                current_tree.set_root(int(token))
                current_tree = path.pop()
            except ValueError:
                raise ValueError("Token '{0}' is not a valid integer".format(token))
        elif token == ')':
            current_tree = path.pop()
        elif token in operators:
            current_tree.set_root(token)
            path.push(current_tree)
            current_tree.insert_right(' ')
            current_tree = current_tree.get_right()

    return parse_tree


def evaluate(parse_tree: BinaryTree):
    if parse_tree.get_right() and parse_tree.get_left():
        left = evaluate(parse_tree.get_left())
        right = evaluate(parse_tree.get_right())

        op = parse_tree.get_root()
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '/':
            return left / right

    else:
        return parse_tree.get_root()


expr = "(3+(4*5))"
p_tree = construct_parse_tree(expr)
print(evaluate(p_tree))
