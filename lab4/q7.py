"""Write a Python class which has two methods get_String and print_String. The
get_String accept a string from the user and print_String print the string in upper
case."""
class strProcess:
    def __init__(self):
        self.user_str = ""

    def get_String(self):
        self.user_str = input("Enter a string: ")

    def print_String(self):
        print(self.user_str.upper())

obj = strProcess()
obj.get_String()
obj.print_String()