from structures.deque import Deque


def check_palindrome(input_string):
    list_input = list(input_string)
    q = Deque()
    is_palindrome = True

    for character in list_input:
        q.add_rear(character)

    for index in range(len(list_input) // 2):
        if is_palindrome:
            front = q.remove_front()
            rear = q.remove_rear()
            is_palindrome = front == rear

    print("Palindrome -> " + str(is_palindrome))


check_palindrome("madam")
check_palindrome("radar")
check_palindrome("level")
check_palindrome("malayalam")
check_palindrome("abcd")
