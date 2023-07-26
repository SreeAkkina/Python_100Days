"""
{key: value}
"""
programming_dictionary = {"bug": "defintion", 
"Function": "definition",
}

#print
print(programming_dictionary["Function"])

#adding new items
programming_dictionary["Loop"] = "dasdfkjsdjfh"
print(programming_dictionary)

#creating empty
empty_dictionary = {}

#edit an item in a dictionary
programming_dictionary["bug"] = "sdjfhsadkjfh"
print(programming_dictionary)

#loop through
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

#wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

