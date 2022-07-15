film_budget = float(input())
number_of_statists = int(input())
price_of_clothing_per_statist = float(input())
total_price_of_clothing = price_of_clothing_per_statist * number_of_statists
decor_price = film_budget * 0.1
if number_of_statists >= 150:
    total_price_of_clothing *= 0.9
total_expenditure = decor_price + total_price_of_clothing
budget_result = film_budget - total_expenditure
if budget_result >= 0:
    print("Action!")
    print(f"Wingard starts filming with {budget_result:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {abs(budget_result):.2f} leva more.")

