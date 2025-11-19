'''
You are given a character string A, having length N and an integer ASCII code B.
You have to tell the leftmost occurrence of the character having ASCII code equal to B, in A or
report that it does not exist.
'''
A= "aabbcc"
B=98
result= A.find(chr(B))   #finding the leftmost occurrence of character having ASCII code B using find() function
print(result)            #printing the result
