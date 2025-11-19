# Write a program to reverse the words present in a string. Check example input/output.

string= "Everyone loves data science"    #given input string
string=string.split()           #splitting the string into words  using split function
print(string[0][::-1], string[1][::-1], string[2][::-1], string[3][::-1])    #reversing each word using slicing and printing them