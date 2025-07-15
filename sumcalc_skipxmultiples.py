'''Write a program to print the sum of 1 to n. While calculating sum, omit the number which
are multiple of x. Note: Use continue concept.'''
num=int(input("enter the num of digits"))
x=int(input("enetr the number who's multiple have to be skipped"))
sum=0
for i in range(1,num+1):
    if i%x==0:
        continue
    sum+=i
print(sum)