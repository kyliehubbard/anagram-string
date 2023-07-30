"""
CISC-121 2023W
Name: Kylie Hubbard
Student Number: 20294570
Email: kylie.hubbard@queensu.ca
Date: 2023-03-15
I confirm that this assignment solution is my own work and conforms to Queen’s
standards of Academic Integrity
"""

def char_prime(my_char):
    """
    -------------------------------------------------------
    Converts an uppercase letter to a unique prime number
    based on the conversion given in the footnote.
    -------------------------------------------------------
    Parameters:
        my_char - a character in ABCDEFGHIJKLMNOPQRSTUVWXYZ
    Returns:
        prime_int = a prime number unique to the letter.
    -------------------------------------------------------
    """
    list_primes = {
        "A": 2, "B": 3, "C": 5, "D": 7, "E": 11, "F": 13, "G": 17, "H": 19, "I": 23, "J": 29, "K": 31, "L": 37, "M": 41,
        "N": 43, "O": 47, "P": 53, "Q": 59, "R": 61, "S": 67, "T": 71, "U": 73, "V": 79, "W": 83, "X": 89, "Y": 97,
        "Z": 101
    }
    return list_primes[my_char]

def primeify(my_string):
    """
    -------------------------------------------------------
    Recursively gives the product of primes corresponding to
    the letters in the string.
    -------------------------------------------------------
    Parameters:
        my_string - any string
    Returns:
        prime_product = the product of all primes for each
        letter.
    -------------------------------------------------------
    """
    if len(my_string) == 0:
        return 1
    else:
        prime_product = char_prime(my_string[0])*primeify(my_string[1:])
        return prime_product

def is_anagram(string1, string2):
    """
    -------------------------------------------------------
    Determines if two strings are anagrams of each other.
    -------------------------------------------------------
    Parameters:
        string1, string2 - any two strings.
    Returns:
        is_anagram = whether or not they are anagrams.
    -------------------------------------------------------
    """
    if primeify(string1) == primeify(string2):
        return True
    # checks to see if number values of primified strings are equivalent
    else:
        return False

def radix_sort(string):
    """
    -------------------------------------------------------
    Sorts prime number equivalent of characters of a string
    in ascending order using radix sort.
    -------------------------------------------------------
    Parameters:
        string - any uppercase string.
    Returns:
        x = list of prime numbers in ascending order.
    -------------------------------------------------------
    """
    # turns string into list with prime number values
    x = [char_prime(i) for i in string]
    radix_var = 10
    placement = 1
    max_num = max(x)
    while placement < max_num:
        buckets = [list() for _ in range(radix_var)]
        for i in x:
            tmp = int((i/placement)%radix_var)
            buckets[tmp].append(i)
        a = 0
        for b in range(radix_var):
            buck = buckets[b]
            for i in buck:
                x[a] = i
                a+= 1
        placement*=radix_var
    return x
