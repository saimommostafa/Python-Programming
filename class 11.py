car_dict = {
    "car1" : {"brand" : "Ford", "model" : "Mustang", "year" : 1964},
    "car2" : {"brand" : "Toyota", "model" : "Supra", "year" : 2004},
    "car3" : {"brand" : "Bugatti", "model" : "Chiron", "year" : 2012}
}

for sl, info in car_dict.items():
    print(sl)
    for details in info.items():
        print(details)

for key, val in car_dict.items():
    print(f"{key} : {val}")