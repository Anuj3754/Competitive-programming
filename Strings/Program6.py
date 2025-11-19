'''
You are given a character string A. You to trim trailing asterisk characters('*') in the string and
print the resultant string.
'''

A= "**h*e*l*lo*"   # given input string
result=A.rstrip('*') # using <str>.rstrip function to trin the character from the right side
print(result)       # print the resultant string