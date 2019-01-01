from structures.stack import Stack
import time


def check_parentheses(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    matcher = {
        '}': '{',
        ']': '[',
        ')': '(',
    }
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in ['(', '[', '{']:
            s.push(symbol)
        elif symbol in [')', ']', '}']:
            if s.is_empty() or matcher[symbol] != s.peek():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.is_empty():
        return True
    else:
        return False


start = time.time()
print(check_parentheses('((a+b))'))
print(check_parentheses('([)]'))
end = time.time()
print('TimeTaken - ' + str((end - start)))


# Check Parentheses from book -
# https://interactivepython.org/runestone/static/pythonds/BasicDS/BalancedSymbols(AGeneralCase).html
def matches(top, bottom):
    opens = '{[('
    closers = "}])"
    return opens.index(top) == closers.index(bottom)


def check_parentheses_bk(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in '{[(':
            s.push(symbol)
        elif symbol in ')]}':
            if s.is_empty() or not matches(s.pop(), symbol):
                balanced = False

        index = index + 1

    if balanced and s.is_empty():
        return True
    else:
        return False


start = time.time()
print(check_parentheses('((a+b))'))
print(check_parentheses('([)]'))
end = time.time()
print('TimeTaken - ' + str((end - start)))
