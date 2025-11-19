'''
Akash likes playing with strings. One day he thought of applying following operations on the
string in the given order:
Concatenate the string with itself.
Delete all the uppercase letters.
Replace each vowel with '#'.
You are given a string A of size N consisting of lowercase and uppercase alphabets. Return the
resultant string after applying the above operations.
NOTE: 'a' , 'e' , 'i' , 'o' , 'u' are defined as vowels.
'''

A = "aeiOUz"      #given input string
A= A+A           #concatenating string with itself
result= ""       #initializing result string
for char in A:   #iterating through each character in string A
    if not char.isupper():          #checking if character is not uppercase
        if char in "aeiou":         #checking if character is vowel
            result += "#"           #replacing vowel with '#'
        else:
            result += char          #adding consonant to result string
print(result)     #printing the result string
