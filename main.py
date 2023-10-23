#importing string library to help with counting letters
import string

# context manager
with open("mydefaults.ini.txt") as ini_file:
    data = ini_file.read()

#Create the beginning of a number count
number_of_letters = 0

#create a variable to store ascii letters
alphabet = string.ascii_letters

#create a list with each line of data from ini file
lines = data.split("\n")

#for loop to count the number of letters in the ini file
for line in lines:
    for letter in line:
        if letter in alphabet:
            number_of_letters += 1
    print(line, number_of_letters)
