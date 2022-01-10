import random

names_string = input("Give me everybody's name separated by a comma, ")

names = names_string.split(", ")

#Get the total numbers of items in the list.
num_items = (len(names))

#generate random numbers between 0 and the last index
random_choice = random.randint(0, num_items-1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to buy the meal today")