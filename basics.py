# cart = 3
# print(cart)
# print("hello world, hyde is back to python heheheh!")
# this is a comment

# concatenation

# first_name = "adam";
# last_name  = " maculrt";

# full_name = first_name + " " + last_name;
# print (full_name)

# variables interpolation

# introduction = f"my name is {first_name} {last_name} i am 7 years old";
# print(introduction)


# find lenght of word


# word = "long word"
# uppercase_word = word.upper()

# print(len(word))
# print(uppercase_word)


# numbers = [1,2,3,4,5]
# copied_numbers = numbers[:]

# copied_numbers.append(6)

# print(numbers)
# print(copied_numbers)


# list_of_animals = ["monkey","baboon","chimp","rhino","giraffe","bear"]

# first_animal,second_animal, *other = list_of_animals

# print(first_animal)
# print(second_animal)


# colors = ["red", "blue", "green"]
# red, blue, *other = colors

# print(red)
# print(blue)
# print(other)


# names_of_people = ["john","ayo","grace","joy","faith","timi","femi"]

# for name, position in enumerate(names_of_people):
#     print(name, position)

# rewrite this logic

# names_of_people = ["john","ayo","grace","joy","faith","timi","femi"]

# index = 0
# for name in names_of_people:
#     print(index, name)
# index+=1


# First method: regular string concatenation ---

# third metthod: fstrings method ---

# first_name = "Anthony"
# last_name = "joshua"

# print(f"hey! my name is {first_name} {last_name} nice to meet you")

# result: hey! my name is Anthony joshua nice to meet you.

# second method: string formatting ---

# print("hey! my name is", first_name, last_name,"nice to meet you")
# print("hey! my name is {0} {1} nice to meet you".format(first_name,last_name))

# print(f"hey! my name is {first_name} {last_name} nice to meet you")

# result: hey! my name is Anthony joshua nice to meet you.


# age = 27
# name = "james"
# message = "eligible" if age >= 18 else "not eligible"

# result = "eligible" if age >= 18 & name == "james" else "not eligible"

# if age >= 18:
#     message = "eligible"
# else:
#     message ="not eligible"

# print(result)


# if age <13:
#     print("you are a child")
# if age <20:
#     print("you are a teenager")
# if age <30:
#     print("you are a youth")
# if age > 40:
#     print("how are you old man")

# if age <13:
#     print("you are a child")
# elif age <20:
#     print("you are a teenager")
# elif age <30:
#     print("you are a youth")
# else:
#     print("how are you old man")


# Python program to demonstrate
# the difference between and, &
# operator

# first_number = 14
# second_number = 4

# print(second_number and first_number)  # first evaluation with "and" operator
# print(second_number & first_number)  # second evaluation with "&" operator

# what is the result

# if 30 == "30":
#     print("a")
# elif "bag" > "fish" and "bag" > "ball":
#     print("b")
# else:
#     print("c")

# rewrite this logic
# count = 0
# for n in range(1,21):
#     if n%2 == 0:
#         print(n)
#         count+=1
# print(f"there are {count} even numbers in 21")


# fizz buzz challenge

# user_input = int(input("enter a number: "))

# def fizz_buzz(input):
#     if (input % 3 == 0) and (input % 5 == 0):
#         return "fizzbuzz"
#     elif input % 3 == 0:
#         return "fizz"
#     elif input % 5 == 0:
#         return " buzz"
#     return input


# print(fizz_buzz(user_input))


# rewrite this program to count the amount of times a color shows up in the dictionary

# favourite_color_of_students = {
#     "Ade": "red",
#     "timi": "blue",
#     "james": "blue",
#     "grace": "blue",
#     "femi": "red",
#     "hyde": "white",
#     "sarah": "green",
#     "naomi": "red",
#     "john": "purple",
# }

# list_of_colors = favourite_color_of_students.values()
# count_colors = {}

# # loop to find number of repeating items
# for color in list_of_colors:
#     if color in count_colors:
#         count_colors[color] += 1
#     else:
#         count_colors[color] = 1

# # loop to print them out
# for color in count_colors:
#     print(f" the list of colors contains {count_colors[color]} instances of {color}")


# for colors in count_colors.items():
#     color, number = colors
#     print(f" the list of colors contains {number} instances of {color}")

# print(color)

# solution
# def check_rep(dict):
#     colors = list(dict.values())
#     for color in set(colors):
#         rep = colors.count(color)
#         print(f"there are {rep} {color} in colors")


# check_rep(favourite_color_of_students)


# favourite_color_of_students = {**favourite_color_of_students, "timi":"red"}
# print(favourite_color_of_students)


# get method
# check = favourite_color_of_students.get("Ade")
# print(check)


# list_of_colors = favourite_color_of_students.values()
# count_colors = {}
# for color in list_of_colors:
#     if color in count_colors:
#         count_colors[color] += 1
#     else:
#         count_colors[color] = 1
# print(count_colors)

# print(color)


# print(list_of_colors)


# list_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(sorted(list_of_numbers))


# in what order would the list be printed out to console?
# lists_of_words = ["Adriel", "apple", "Boa", "POT", "pineapple", "yacht", "people"]
# print(sorted(lists_of_words))


# # swapp two variables

# boy_name = "Kamala Harris"
# girl_name = "Donald trump"


# empty = girl_name
# girl_name = boy_name
# boy_name = empty

# print(girl_name)
# print(boy_name)

# simpler solution

# boy_name, girl_name = girl_name,boy_name

# classes


# class Animal:
#     planet_lived = "Earth"

#     def __init__(self, name, age, habitat, food):
#         self.name = name
#         self.age = age
#         self.habitat = habitat
#         self.food = food

#     def eating(self):
#         print(f"{self.name} is now eating {self.food}")


# baboon = Animal("baboon", 10, "jungle", "bananas")

# what is the differnce between A and B

# print(Animal.planet_lived)  # A
# print(baboon.food)  # B

# import random


# def plus_one(number):
#     return number + 1


# def function_call(function):
#     number_to_add = 5
#     return function(number_to_add)


# print(function_call(plus_one))

# decorators

# def create_random_fact(function):
#     facts = [
#         "you look cute when you smile",
#         "you dress like royalty",
#         "you are a charming beauty",
#         "you deserve all the good things of life and more",
#         "you never keep a grudge",
#         "nothing ever bothers you",
#     ]

#     random_fact = random.randint(0, len(facts))

#     def tell_random_fact():
#         funct = function()
#         name, age = funct
#         print(
#             f"{name} we celebrate you as you turn {age} today because {facts[random_fact]} "
#         )

#     tell_random_fact()


# @create_random_fact
# def get_name_age():
#     name = input("what is your name: ")
#     age = input("what is your age: ")
#     return [name, age]


# print(get_name_age())

# create_random_fact(get_name_age)


# space junkie


# create a class that greets inhabitants of other planets


# list comprehensions

# rewrite code to be simpler

# price_list = [30, 45, 89, 56, 12]
# new_list = []
# for price in price_list:
#     double_price = price * 2
#     new_list.append(double_price)

# price_list = [*new_list]


# print(price_list)


# # solution
# price_list = [price*2 for price in price_list]
# print(price_list)

# get square of even numbers
# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# squared_even_numbers = []
# for number in number_list:
#     if number % 2 == 0:
#         squared_even_numbers.append(number**2)

# print(squared_even_numbers)


# solution

# squared_even_numbers = [number**2 for number in number_list if number % 2 == 0]
# print(squared_even_numbers)


# write a program that returns the number of vowels in the list of words below
# the output on the console should look like this: xnumber vowels appeared in baby


# words = ["baby", "horse", "Brother bernard", "Angela", "perfume", "Onos", "kranos"]


# def find_vowels(word) -> str:
#     list_vowels = ["a", "e", "i", "o", "u"]
#     vowel_count = sum(1 for letter in word.lower() if letter in list_vowels)
#     return f"{vowel_count} vowels appeared in {word}\n"


# results_mapped = list(result for result in (map(find_vowels, words)))

# print(*results_mapped)


# list_of_numbers =[1,2,3,4,5,6,7,8,9]

# count = sum(1 for number in list_of_numbers)

# print(count)


# grades = ["a", "b", "c", "a", "f", "f"]

# remove_f = sorted(grade for grade in grades if grade != "f")

# print(remove_f)


# items = [("product 1", 30), ("product 2", 10), ("product 3", 12), ("product 4", 50)]

# items = sorted(items, key = lambda item: item[1])


# items.sort(key = lambda item: item[1])
# print(items)

# def sort_item(item) -> int:
#     return item[1]

# items.sort(key = sort_item)
# print(items)

# # map again by mosh
# items = [("product 1", 30), ("product 2", 10), ("product 3", 12), ("product 4", 50)]

# items = list(map(lambda item: item[1], items))

# print(items)

# filter
# items = [("product 1", 30), ("product 2", 10), ("product 3", 12), ("product 4", 50)]

# items = [item for item in items if item[1] > 10]

# print(items)



from Market_challenge.app import get_user_input


get_user_input()