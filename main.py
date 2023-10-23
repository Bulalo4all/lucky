#importing string library to help with counting letters
import string

# context manager
with open("mydefaults.ini.txt") as ini_file:
    data = ini_file.read()

#Create the beginning of a letter count and number count
number_of_letters = 0
number_of_numbers = 0

#create a variable to store ascii letters and digits
alphabet = string.ascii_letters
number_0_to_nine = string.digits

#create a list with each line of data from ini file
lines = data.split("\n")

#for loop to count the number of letters and digits in the ini file
for line in lines:
    for letter in line:
        if letter in alphabet:
            number_of_letters += 1
        elif letter in number_0_to_nine:
            number_of_numbers += 1
            
print(number_of_letters, number_of_numbers)
