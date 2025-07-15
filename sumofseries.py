'''Mahesh is interested in finding the sum of a certain series. Write a program to obtain the
values of x and n and find the sum of the following series.
1-x+x^2-x^3+.....x^n'''
x=int(input("enetr the value of x"))
n=int(input("enetr the number of terms"))

sum=0
term=0
for i in range(n+1):
    term=(-1)**i * (x**i)
    sum+=term
print("the sum of the series =",sum)