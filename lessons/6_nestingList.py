capitals = {
    "France": "paris",
    "Germany": "Berlin"
}

#nesting a list in dictionary
travel_log = {
    "France": ["paris", "lille", "dijon"],
    "Germany": ["berlin", "hamburg", "stuttgart"],
}

#nesting a list in a list
["a", "b", ["2", "3"]]

#nesting dictionary in a dictionary
travel_log = {
    "france": {"cities_visited": ["paris", "lille", "dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["berlin", "hamburg", "stuttgart"], "total_visits": 5}
}

#nesting dictionary in a list
travel_log = [
    {
     "country": "france", 
     "cities_visited": ["paris", "lille", "dijon"], 
     "total_visits": 12
    },
    {
     "country": "Germany", 
     "cities_visited": ["berlin", "hamburg", "stuttgart"], 
     "total_visits": 5
     },
]