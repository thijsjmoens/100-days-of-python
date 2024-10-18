travel_log = {
    "France": ["Paris", "Lille", "Nice"],
}

# print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]

# print(nested_list[2][1])

new_travel_log = {
    "France" : {
        "number_of_times_visited": 2,
        "cities_visited": ["Paris", "Nice", "Lille"],
    },
}

print(new_travel_log["France"]["cities_visited"][0])   