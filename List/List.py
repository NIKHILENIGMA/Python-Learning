
#* Creating a List 

my_list = [1, "Hello", 3.14]
print(my_list)
# [1, "Hello", 3.14]


#* Accessing List Items
print(f'Accessing first list items: {my_list[0]}')
# Accessing first list items: 1


#* Modifying Lists
my_list[1] = "World"
print(my_list)  
# Output: [1, "World", 3.14]


#* Adding Items
my_list.append("Python")
print(my_list)  
# [1, 'World', 3.14, 'Python']


my_list.insert(1, "there")
print(my_list)  
# Output: [1, "there", "World", 3.14, "Python"] 

#note new_list[start:stop:step]

new_list = [0,1,2,3,4,5,6,7,8,9]

print(new_list[0:10:3])
# [0, 3, 6, 9]

print(new_list[0:])
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(new_list[:5])
#[0, 1, 2, 3, 4]

print(new_list[::2])
# [0, 2, 4, 6, 8]

print(new_list[::-1])
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


