'''Arav buys an old scooter for Rs. A and spends Rs. B on its repairs. If he sells the scooter for
Rs. C , what is his gain %? Write a program to compute the gain %.
Output displays the gain percentage. Format the output to 2 decimal places.'''
oldrate=float(input("enter the old rate"))
repair=float(input("what is the repair cost"))
saleprice=float(input("enter the sale price"))
totalprice=(oldrate+repair)
gain=(saleprice-totalprice)
print(gain)
gainpercent=(gain/saleprice)*100
print(f"the gain percent is {gainpercent} ")

