fuel_type = input()
litres_fuel = float(input())
discount_card = input()
price_fuel = 0
price_gasoline = litres_fuel * 2.22
price_diesel = litres_fuel * 2.33
price_gas = litres_fuel * 0.93
if discount_card == "Yes":
    price_gasoline = litres_fuel * (2.22 - 0.18)
    price_diesel = litres_fuel * (2.33 - 0.12)
    price_gas = litres_fuel * (0.93 - 0.08)
if fuel_type == "Gasoline":
    price_fuel = price_gasoline
elif fuel_type == "Diesel":
    price_fuel = price_diesel
elif fuel_type == "Gas":
    price_fuel = price_gas
if 20 <= litres_fuel <= 25:
    price_fuel *= 0.92
elif litres_fuel > 25:
    price_fuel *= 0.9
print(f"{price_fuel:.2f} lv.")