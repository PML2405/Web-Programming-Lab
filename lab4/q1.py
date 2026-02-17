# Write a python program to reverse a content a file and store it in another file.
file=open("q1_input.txt","r")

data=file.read()

new_file=open("q1_output.txt","w")

new_file.write(data[::-1])