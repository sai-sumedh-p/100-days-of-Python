
P=float(input("enter the principle amount"))
R=float(input("enter the intrest rate"))
T=int(input("enter the time in years"))
SI=(P*T*R)/100
print(f"The Simple Intrest is {SI}")
total=P+SI
print(f"the total payable amount is : {total}")