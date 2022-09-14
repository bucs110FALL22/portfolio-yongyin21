import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
print(type(cost_per_week))
classes_per_week = 3
print("classes per week" ,classes_per_week,)
print(type(classes_per_week))
cost_per_class = ((cost_per_week/classes_per_week))
print("Your incredibly high cost per class:",cost_per_class)
print(type(cost_per_class))



#Part B
shoppinglist = ["pizza", "chicken", "fish", "tofu", "cheese"]
randys = random.choice(shoppinglist)
print(randys)