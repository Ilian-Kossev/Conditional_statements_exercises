fuel_type = input()
fuel_litres = float(input())
result = ""
if fuel_type == "Diesel" or fuel_type == "Gasoline" or fuel_type == "Gas":
    if fuel_litres < 25:
        if fuel_type == "Diesel":
            result = "diesel"
        elif fuel_type == "Gasoline":
            result = "gasoline"
        elif fuel_type == "Gas":
            result = "gas"
        print(f"Fill your tank with {result}!")
    elif fuel_litres >= 25:
        if fuel_type == "Diesel":
            result = "diesel"
        elif fuel_type == "Gasoline":
            result = "gasoline"
        elif fuel_type == "Gas":
            result = "gas"
        print(f"You have enough {result}.")
else:
    print("Invalid fuel!")

