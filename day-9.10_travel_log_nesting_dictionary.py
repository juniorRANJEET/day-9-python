# you are going to write a program that add to a travel_log.
# you can see a travel_log which is a list that contain 2 dictionaries
# write a function that will work to add the entry for Delhi to the travel_log
# add_new_state("Delhi",2,["mahipalpur","okhala","karol Bag","nehru place","mehrauli","badarpur"]
#nesting a dictionary into a list
travel_log = [
    {
    "state":"Bihar",
    "city": ["Darbhanga","patna","gaya","nalanda"],
    "visit": 10
    },
    {
    "state":"Maharashtra",
    "city": "Pune",
    "visit" :1
    }
]
def add_new_state(state_visited,cities_visited,times_visited):
    new_state = {}
    new_state["state"] = state_visited
    new_state["city"] = cities_visited
    new_state["visit"] = times_visited
    travel_log.append(new_state)
add_new_state("Delhi",["mahipalpur","okhala","karol Bag","nehru place","mehrauli","badarpur"],5)

print(travel_log)