'''Create a list of six school subjects. Ask the user which of these subjects they dont like.
Delete the subject they have chosen from the list before you display the list again. 
'''
subjects=[]
for i in range(1,6):
    sub=input("enter you subject name")
    subjects.append(sub)
print("your subjects are",subjects)
dislike=input("enter the subject that you dislike")
if dislike in subjects:
    subjects.remove(dislike)
print("your final subject are",subjects)