# dictionary looks like a form of TABLE . it have KEY and VALUE
# when ever you want to print dictionaries values you have to write syntax:
# print(programing_dictionary["keys"])

# let understand some question

programming_dictionaries = {
#   "KEYS": "VALUES"
    "name": "My name is RANJEET. ",
    "birth city": "My city is Benipur. ",
    "current location": "My current location is Darbhanga .",
    123: "its my mobile number" # only 123 without sting can be KEY
}
# retriving items from the dictionary
print(programming_dictionaries["current location"]) # KEYS should be in string format
print(programming_dictionaries[123])