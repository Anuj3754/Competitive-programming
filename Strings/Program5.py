'''
You are given a character string A. You to trim leading asterisk characters('*') in the string and
print the resultant string.
'''

A="**h*e*l*lo*"    #given input string
result=A.lstrip("*")     #using <str>.lstrip function to trin the charcter from the left side
print(result)           # print the resultant string