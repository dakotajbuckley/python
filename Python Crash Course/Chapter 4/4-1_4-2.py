# 4.1 Pizzas
pizzas = ["stuffed crust", "pepperoni", "bbq", "cheese", "hawaiian", "sausage", "chicken", "margarita", "extra pepperoni"]
for pizza in pizzas:
    print("I enjoy eating " + pizza + " pizza!")
print("I hope this goes to show just how much I like Pizza!")

# 4.2 Pizzas
animals = ["otters", "beavers", "polar bears"]
for animal in animals:
    print(animal.title() + " love to play in the water!")
print("Any of these animals enjoy playing in the water!")

# 4.10
print("The first three items in the list are: " + str(pizzas[0:3]))
print("Three items from the middle of the list are: " + str(pizzas[3:6]))
print("Three items from the middle of the list are: " + str(pizzas[6:9]))

friend_pizzas = pizzas[:]
friend_pizzas.append("spicy")
pizzas.append("tasty")
print(pizzas)
print(friend_pizzas)

for pizza in friend_pizzas:
    print(pizza)

for animal in animals:
    print(animal)