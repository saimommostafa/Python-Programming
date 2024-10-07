tmp = float(input("Enter the temperature: "))
Cunit = input("Enter the unit it is in. Cel, Far, Kel (C/F/K): ")
Punit = input("Enter the unit in which you want to convert. Cel, Far, Kel (C/F/K): ")

if Cunit == "C" and Punit == "F":
    result = (tmp * 9/5) + 32
    print("\nTemperature in Fahrenheit is: ", round(result, 2))

elif Cunit == "F" and Punit == "C":
    result = (tmp - 32) * 5/9
    print("\nTemperature in Celsius is: ", round(result, 2))

elif Cunit == "C" and Punit == "K":
    result = tmp + 273.15
    print("\nTemperature in Kelvin is: ", round(result, 2))

elif Cunit == "K" and Punit == "C":
    result = tmp - 273.15
    print("\nTemperature in Celsius is: ", round(result, 2))

elif Cunit == "F" and Punit == "K":
    result = (tmp - 32) * 5/9 + 273.15
    print("\nTemperature in Kelvin is: ", round(result, 2))

elif Cunit == "K" and Punit == "F":
    result = (tmp - 273.15) * 9/5 + 32
    print("\nTemperature in Fahrenheit is: ", round(result, 2))

else:
    print("\nOne or both of the scale you selected is not valid")