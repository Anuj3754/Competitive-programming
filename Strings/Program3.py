'''
Write a program to input T strings (S) from user and print 1 if it is palindrome otherwise print 0.
NOTE:A string is palindrome if it reads the same from backward as from forward.
'''
T= int(input())
result=[]
for i in range(T):
    s= input()
    if s==s[::-1]:
        result.append(1)
    else:
        result.append(0)
for r in result:
    print(r)