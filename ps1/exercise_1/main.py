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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
