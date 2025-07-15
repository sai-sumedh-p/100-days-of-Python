'''Quiz Bee is a famous quiz Competition that tests students on a wide variety of academic
subjects. This weeks competition was a Team event and students who register for the event
will be given a unique registration code N. The participants are teamed into different teams
and the team to which a participant is assigned to depend on the absolute difference between
the first and last digit in the registration code N.'''
reg=(input("enter the registration number"))
if len(reg)<=9:
    print("enter a valid input of 10 digits")
    
else:
    num=abs(int(reg[0])-int(reg[-1]))
    print("team number =",num)
