#6.1
# coy = {"first_name": "coy", "last_name": "sollis", "city": "lehi", "age": 24}

# # 6.2
# favorite_numbers = {"coy": 24, "dakota": 7, "korbin": 35, "wes": 17, "rocky": 74}
# for name, num in favorite_numbers.items():
#     print(name + "'s favorite number is " + str(num))

#6.3
words = {
    "immutable": "a value cant be changed",
    "for loop": "loop through a certain number of times",
    "variable": "a place to store pieces of data",
    "dictionary": "a list of key value pairs",
    "if statement": "a way to check for conditions",
}

# 6.4
for word, definition in words.items():
    print(word + ": " + definition)

# 6.5
rivers = {"provo river": "orem", "nile": "egypt", "colorado": "colorado"}
for river, country in rivers.items():
    print("The " + river + " runs through " + country)
for river in rivers.keys():
    print(river)
for country in rivers.values():
    print(country)

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
'dakota': '',
'coy': 'coyql',
'austin': ''
}
for person, language in favorite_languages.items():
    if language:
        print("Thank you for responding " + person)
    else:
        print("Please take the poll " + person)