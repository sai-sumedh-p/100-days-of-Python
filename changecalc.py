'''Shekar, an enthusiastic kid visited the fair along with his family. His father wanted him to
purchase entry tickets from the counter for his family members. Being a little kid, he is just
learning to understand about units of money. Shekar has paid some amount of money for the
tickets but he wants your help to give him back the change of Rs. N using the minimum number
of rupee notes.
Consider a currency system in which there are notes of seven denominations, namely, Rs. 1,
Rs. 2, Rs. 5, Rs. 10, Rs. 50, Rs. 100. If the change given to Shekar Rs. N is input, write a
program to compute the smallest number of notes that will combine to give Rs. N.
Output should display the smallest number of notes that will combine to form N.'''
money=int(input("how much change did you get?"))
n100=int(money/100)
print(n100,"hundred rupee notes")
money=(money%100)
print("remaining money =",money)
n50=int(money/50)
print(n50,"50 rupee notes")
money=(money%50)
print("remaining money =",money)
n20=int(money/20)
print(n20,"20 rupee notes")
money=(money%20)
print("remaining money =",money)
n10=int(money/10)
print(n10,"10 rupee notes")
money=(money%10)
print("remaining money =",money)
n5=int(money/5)
print(n5,"5 rupee notes")
money=(money%5)
print("remaining money =",money)
n2=int(money/2)
print(n2,"2 rupee notes")
money=(money%2)
print("remaining money =",money)
n1=int(money/1)
print(n1,"1 rupee notes")
money=(money%1)
print("remaining money =",money)