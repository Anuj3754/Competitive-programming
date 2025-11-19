'''
You are given two character strings A and B.
You have to find the first occurrence of string B in string A, as a substring, and return the starting
position of first occurrence.
A substring is a contiguous sequence of characters within a string. For e.g "at" is a substring in
"catalogue".
'''
A = "aabababaa"
B = "ba"
result = A.find(B)   #finding the first occurrence of string B in string A using find() function
print(result)        #printing the result