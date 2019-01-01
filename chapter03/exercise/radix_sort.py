def get_digit(number, pos):
    if pos < 0:
        return 0
    else:
        return int(str(number)[pos])


#  Time complexity -> O ( n +  k(n + 10) )
def radix_sort(numbers):
    bin_main = numbers.copy()
    numeric_bins = [[] for _ in range(10)]

    max_char_length = 0
    for number in numbers:
        length = len(str(number))
        if length > max_char_length:
            max_char_length = length

    for index in range(max_char_length):
        while len(bin_main) > 0:
            number = bin_main.pop(0)
            pos = len(str(number)) - index - 1
            digit = get_digit(number, pos)
            numeric_bins[digit].append(number)

        for i in range(len(numeric_bins)):
            bin_main.extend(numeric_bins[i])
            numeric_bins[i] = []

        # print("index -> {} , main_bin -> {}".format(index, bin_main))

    print(bin_main)


radix_sort([899, 20, 100, 495, 8999])
radix_sort([170, 45, 75, 90, 802, 24, 2, 66])
