from chapter06.ParseTree import construct_parse_tree
from structures.BinaryTree import BinaryTree


def preorder(parse_tree: BinaryTree):
    pre_list = ''
    pre_list += str(parse_tree.get_root())
    if parse_tree.get_left() is not None:
        pre_list += preorder(parse_tree.get_left())
    if parse_tree.get_right() is not None:
        pre_list += preorder(parse_tree.get_right())

    return pre_list


def postorder(parse_tree: BinaryTree):
    post_list = ''
    if parse_tree.get_left() is not None:
        post_list += postorder(parse_tree.get_left())
    if parse_tree.get_right() is not None:
        post_list += postorder(parse_tree.get_right())

    post_list += str(parse_tree.get_root())

    return post_list


def inorder(parse_tree: BinaryTree):
    in_list = ''
    if parse_tree.get_left() is not None:
        in_list += '('
        in_list += inorder(parse_tree.get_left())

    in_list += str(parse_tree.get_root())

    if parse_tree.get_right() is not None:
        in_list += inorder(parse_tree.get_right())
        in_list += ')'
    return in_list


expr = "(3+(4*5))"
p_tree = construct_parse_tree(expr)
print(preorder(p_tree))
print(postorder(p_tree))
print(inorder(p_tree))
