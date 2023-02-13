programming_dictionaries = {
#   "KEYS": "VALUES"
    "name:": "My name is RANJEET. ",
    "birth city:": "My city is Benipur. ",
    "current location:": "My current location is Darbhanga ."
}
# print(programming_dictionaries)
# loop through a dictionary
for things in programming_dictionaries:
    print(things) # it actually prints all KEYS in form of list, not KEYS and VALUE

for things in programming_dictionaries:
    print(programming_dictionaries[things]) # here it print all VALUES in the form of list not KEYS