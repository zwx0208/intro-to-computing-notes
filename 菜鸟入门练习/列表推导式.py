shopping_list = ["apple", "eggs", "milk", "banana", "tea"]
shopping_list1=[things.upper()for things in shopping_list if len(things)>=4]
print(shopping_list1)