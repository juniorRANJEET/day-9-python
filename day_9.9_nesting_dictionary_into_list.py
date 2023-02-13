#nesting a dictionary into a list
travel_log = [
    {
    "state":"Bihar",
    "city_visited": ["Darbhanga","patna","gaya","nalanda"],
    "total_visited": 8
    },
    {
    "state":"Gujrat",
    "city_visited": ["Ahmedabad","surat","rajkot"],
    "total_visited" :2
    },
    {
    "state":"Maharashtra",
    "city_visited": "Pune",
    "total_visited" :1
    }
]
print(travel_log)
print(travel_log[2])