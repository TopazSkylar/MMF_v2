import random

fruit_list = ['apple', 'banana', 'cherry', 'dragonfruit']
color_list = ['green', 'yellow', 'red', 'pink']

first_fruit = random.choice(fruit_list)

# find the position of the selected item
fruit_index = fruit_list.index(first_fruit)

first_color = color_list[fruit_index]

print(f"first fruit: {first_fruit} | first color: {first_color}")