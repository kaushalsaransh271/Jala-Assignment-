#1. Write a program to read text file
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

#2. Write a program to write text to .txt file using InputStream
text = input("Enter text: ")

file = open("output.txt", "w")
file.write(text)
file.close()

print("Data written successfully")

#3. Write a program to read a file stream
file = open("sample.txt", "r")

for line in file:
    print(line)

file.close()

#4. Write a program to read a file stream that supports random access
file = open("sample.txt", "r")

file.seek(0)        # move cursor
print(file.read(10))  # read first 10 characters

file.close()

#5. Write a program to read a file at a particular index using
file = open("sample.txt", "r")

file.seek(5)     # move to index 5
print(file.read())

file.close()

#6. Write a program to check whether a file has read & write access permissions
import os

filename = "sample.txt"

print("Read Access:", os.access(filename, os.R_OK))
print("Write Access:", os.access(filename, os.W_OK))
