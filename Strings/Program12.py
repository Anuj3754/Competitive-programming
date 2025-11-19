# Print 1 if all the characters of a character array are alphanumeric (a-z, A-Z, and 0-9) else, print 0.

A= "Python45"           #given input string
if A.isalnum():         #checking alphanumeric using isalnum() function
    print(1)            #printing 1 if true
else:                   #printing 0 if false
    print(0)            #printing 0