'''Ask the user to enter four of their favourite foods and store them in a dictionary so that they
are indexed with numbers starting from 1. Display the dictionary in full, showing the index
number and the item. Ask them which they want to get rid of and remove it from the list. Sort
the remaining data and display the dictionary.'''
food_dict={}
for i in range(1,5):
    food=input("enter you favourite food")
    food_dict[i]=food
for index,item in food_dict.items():
    print(f"{index}. {item}")
num=int(input("enter the index number of the food that you want to delete"))
del food_dict[num]
print("the updated data\n")
for index,item in food_dict.items():
    print(f"{index}. {item}")
sorted_foods=sorted(food_dict.values())
new_foods = {i+1: sorted_foods[i] for i in range(len(sorted_foods))}
print("\nUpdated food list:")
for key in new_foods:
    print(f"{key}. {new_foods[key]}")
