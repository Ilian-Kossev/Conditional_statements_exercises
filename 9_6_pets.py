from math import floor, ceil

number_of_days = int(input())
kg_food_left = int(input())
dog_food_kg_daily = float(input())
cat_food_kg_daily = float(input())
turtle_food_gr_daily = float(input())
kg_food_needed = (dog_food_kg_daily + cat_food_kg_daily + turtle_food_gr_daily / 1000) * number_of_days
difference = kg_food_left - kg_food_needed
if difference >= 0:
    print(f"{floor(difference)} kilos of food left.")
else:
    print(f"{ceil(abs(difference))} more kilos of food are needed.")

