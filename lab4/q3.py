#Write a python program to sort words in alphabetical order.
strings_input=input("Enter the words separated by space: ")

words=strings_input.split(' ')
words.sort(key=str.lower)
print(words)