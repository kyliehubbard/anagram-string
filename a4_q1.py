"""
CISC-121 2023W
Name: Kylie Hubbard
Student Number: 20294570
Email: kylie.hubbard@queensu.ca
Date: 2023-03-15
I confirm that this assignment solution is my own work and conforms to Queen’s
standards of Academic Integrity
"""

from functions4 import is_anagram, primeify, radix_sort

x = " " # for quality of life

print("Hello! Welcome to the program. This program takes two strings and determines if they are anagrams of each other!")

while True:
    first_string = input("What is the first string you would like to input? Please type in all uppercase.\n")
    if first_string.isupper() == True:
        print("This is valid!")
        while True:
            second_string = input("What is the second string you would like to input? Please type in all uppercase.\n")
            if second_string.isupper() == True: # to determine if the strings are uppercase
                print("This is valid!")
                print(x)
                print("The answer to if these strings are anagrams is: " + str(is_anagram(first_string, second_string)))
                print(x)
                if primeify(first_string) == primeify(second_string): # to check if the strings are the same for radix sort
                    print("The sorted prime values for the string/anagram is: " + str(radix_sort(first_string)))
                else:
                    print("The sorted prime values corresponding to each character for the first string is: "
                          + str(radix_sort(first_string)))
                    print("The sorted prime values corresponding to each character for the second string is: "
                          + str(radix_sort(second_string)))
                break
            else:
                print("This is invalid. Please try again.")
                continue
        break
    else:
        print("This is invalid. Please try again.")
        continue
