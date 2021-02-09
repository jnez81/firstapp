"""
There is a string,s, of lowercase English letters that is repeated infinitely many times. 
Given an integer, n, find and print the number of letter a's in the first  letters of the infinite string.

Example
s = 'abcac'
n = 10

The substring we consider is abcacabcac, the first 10 characters of the infinite string. There are 4 
occurrences of a in the substring.

Function Description

Complete the repeatedString function in the editor below.

repeatedString has the following parameter(s):

s: a string to repeat
n: the number of characters to consider
Returns

int: the frequency of a in the substring
Input Format

The first line contains a single string,s.
The second line contains an integer, n.
"""

def repeatedString(s, n):
    # Initialize substring 
    substring = s 

    # Iterate over characters in string 's'
    i = 0

    # While loops to concantenate substrings and characters
    while (len(substring) <= (n - len(s))):
        substring += s
        continue

    while len(substring) <= n-1:
        addChar = str(s[i])
        substring += addChar
        i += 1
        continue

    return substring.count('a')
        


print(repeatedString('aba', 10))