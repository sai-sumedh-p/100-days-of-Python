'''.Ram participated in a competition in which he has to find the sum of digits of a number
within a short period. Write a program to find the sum of digits of a number given by the
user'''
num=(input("enter the number"))
digit_sum=0
for digit in num:
    digit_sum+=int(digit)

print(digit_sum)