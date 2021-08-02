# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def get_name() -> str:
    """
    this function gets name of the user
    :return:
    """
    name = input("What's your name?")
    return name


def wellcom():
    print("Wellcom! Get comfortable")


def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {get_name()}')  # Press Ctrl+F8 to toggle the breakpoint.
    wellcom()


def main():
    # add main function.
    print_hi()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
