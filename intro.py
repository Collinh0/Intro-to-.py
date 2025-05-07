'''
Rules associated with variables
1. Naming convention is snake case
2. Cannot use keywords
3.Variables cannot start with a number
4. Use identation to define code blocks
5.have descriptive variable names
'''
"""
1. dicts
2. strings
3. lists
4. tuples
5. sets
6. integers
7. floats
8. booleans
9. None

"""

# Strings
message = "Intro to python"
greeting = str("Jane")

#Interpolation in py
first_name = "John"
full_name = f"{first_name} Doe"
print(full_name)

# Integers and Floats
total = 0.7 + 2.5
print (total)
print (type(total))
print (type(7/3))

print (int(2.5 +1.4))

cost = 12.5

# Booleans\
is_adult = True
#boolean expression -> a logical statement that evaluates to True or False
#logical operators -> and, or, not
#comparison operators -> ==, !=, >, <, >=, <=
#numeric operators -> +, -, *, /, //, %, **

print(bool(""))
print(bool(0))

print (4 > 9)

# 5. dictionaries
# A dictionary is a collection of key-value pairs
# A dictionary is created using curly braces {}
# A dictionary is mutable
# A dictionary can contain any data type
# A dictionary can contain duplicate keys
person = { "name" : "Collins",
          "age": "23",
          "adress" : {
            "city" : "Nairobi",
            "country" : "Kenya"
          }
  }
  #square brackets or .get() method are used to access the values in a dictionary
print(person["name"])

   #get method
print(person.get("name"))
print(person.get("age"))

#Adding or updating dicts -> as long as the key exist,it is going to do an update
#else is not going to add
#modify age
student = {
    "name": "Collo Muani",
    "age": 23,
    "location": "Nairobi",
    "country": "Kenya",
    "major": "Software Engineering"
}
student["age"] = 25

#Adding a new key-value pair
student["class"] = {
    "name": "Web 9",
    "location": "remote"
}

print(student)
del student["location"]

#the pop gives you back the deleted value
deleted_value = student.pop("class")



# 6.List -> array
colors = ["red", "green", "blue"]
# A list is a collection of items
print(colors[0])
# A list is mutable
#tuple is immutable

#2. sets -> unique elements -> we  can create sets using curly braces {} or tge set () constructor
random_values = {2,3,4,3,2,4,5}
print(random_values)

#empty curly braces still fall under dicts
empty_set = {}
print(type(empty_set))
#to create an empty set, we use the set() constructor
correct_empty_set = set([2,3,4,3])  #-> a set only accepts one argument,so covert ito a list using[]

#3. Lists
#ordered collection of items,similar to arrays
#lists are mutable
students = [{"score":49, "name":"Collins"},{"score": 50, "name":"Ashley"},{"score": 60, "name":"Nancy"}]

#how to get the length of a list
print("Length of the list: ", len(students))

scores = [490, 500, 610]
scores[1] = 50
#this gives an error
#scores[5] = 90

scores.insert(5, 90)
scores.insert(3 , 80)

#map method
def multiply_by_two(x):
    return x * 2

map_iterator = map(multiply_by_two, scores)
print("Multiplied scores: ", list(map_iterator))

multiplied_scores = list(map_iterator)

#Filtering
print("Filtered scores",list(filter(lambda x: x > 100, multiplied_scores)))

#4. tuples -> similar to lists but immutable and we use parentheses ()

emails = ['collo@gmail.com', 'happy@gmail.com']
emails[1] = 'ndegwa@gmail.com' # --> this gives an error (immutable)

temp_emails = list(emails)
temp_emails[1] = 'ndegwa@gmail.com'
modified_emails = tuple(temp_emails)
print(modified_emails)