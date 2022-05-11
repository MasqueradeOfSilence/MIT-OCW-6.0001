# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def is_odd(num):
    return num % 2 != 0


def get_largest_odd_number(x, y, z):
    odd_numbers = []
    if is_odd(x):
        odd_numbers.append(x)
    if is_odd(y):
        odd_numbers.append(y)
    if is_odd(z):
        odd_numbers.append(z)
    if len(odd_numbers) > 0:
        print(max(odd_numbers))
    else:
        print("No odd numbers")


def print_xs():
    num_xs = int(input("How many times should I print the letter X? "))
    to_print = ""
    # concatenate X to toPrint numXs times
    num_iterations = 0
    while num_iterations < num_xs:
        to_print += "X"
        num_iterations += 1
    print(to_print)


def print_largest_odd_of_10(list_of_ten):
    if len(list_of_ten) != 10:
        print("Not 10 items")
        # we shouldn't have to fail here with the for loop, though
        # because 10 is pretty arbitrary; it should work with any number
    odd_numbers = []
    for item in list_of_ten:
        if is_odd(item):
            odd_numbers.append(item)
    if len(odd_numbers) == 0:
        print("No odd numbers!")
    else:
        print(max(odd_numbers))


def is_mathematical_decimal(num_str):
    if len(num_str) == 0:
        return False
    if num_str[0] == "-":
        num_str = num_str[1:]
    for char in num_str:
        if not char.isnumeric() and not char == ".":
            return False
    return True


def sum_string_of_decimals(string_of_decimals):
    # example: '1.23,2.4,3.123' = 6.753
    to_return = 0
    split = string_of_decimals.split(",")
    for num in split:
        if not is_mathematical_decimal(num):
            break
        to_return += float(num)
    return to_return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # Expected: 5
    get_largest_odd_number(4, 5, 6)
    # Expected: none
    get_largest_odd_number(2, 4, 8)
    # Expected: 11
    get_largest_odd_number(1, 5, 11)
    # Expected: -1
    get_largest_odd_number(-5, -3, -1)
    print_xs()
    # Expected: 1 and error message
    print_largest_odd_of_10([1])
    # Expected: error message
    print_largest_odd_of_10([])
    # Expected: error message
    print_largest_odd_of_10([4, 6, 8, 2, 22, 24, 26, 28, 30, 100000])
    # Expected: 9999999
    print_largest_odd_of_10([5, 7, 9, 9999999, -5, 4, 2, 1, 0, 1925])
    # Expected: 19
    print_largest_odd_of_10([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])
    # Expected: 9999999.1 and error message
    print_largest_odd_of_10([5, 7, 9, 9999999, -5, 4, 2, 1, 0, 1925, 9999999.1])
    # Expected: '1.23,2.4,3.123' = 6.753
    print(sum_string_of_decimals('1.23,2.4,3.123'))
    # Expected: 0
    print(sum_string_of_decimals(''))

    # is_mathematical_decimal test cases:
    # Expected: True
    print(str(is_mathematical_decimal("1.23")))
    # Expected: True
    print(str(is_mathematical_decimal("123")))
    # Expected: True
    print(str(is_mathematical_decimal("-1.23")))
    # Expected: False
    print(str(is_mathematical_decimal("1.-23")))
    # Expected: False
    print(str(is_mathematical_decimal("1.23aaaa")))
    # Expected: False
    print(str(is_mathematical_decimal("z")))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
