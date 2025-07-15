'''Create a tuple containing the names of five countries and display the whole tuple. Ask the
user to enter one of the countries that have been shown to them and then display the index
number (i.e. position in the list) of that item in the tuple'''
countries = ("India", "Canada", "Japan", "Brazil", "Germany")

y=input("enter the country's name that you want index number of")
if y in countries:
    print(countries.index(y))
else:
    print("the mentioned country is not there in the tuple")