'''Write a python program to print the string until it meets a particular element.'''
str=input("enter the string")
ch=input("enetr the character you want to stop at")
for i in str:
    if i==ch:
        break
    print(i)
    
        

    