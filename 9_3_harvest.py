from math import floor, ceil

square_metres_vineyard = int(input())
kg_grapes_per_square_meter = float(input())
litres_needed_for_winemaking = int(input())
number_of_workers = int(input())
kg_grapes_produced = square_metres_vineyard * kg_grapes_per_square_meter
litres_wine_produced = kg_grapes_produced * 0.4 / 2.5
litres_wine_result = litres_wine_produced - litres_needed_for_winemaking
if litres_wine_result < 0:
    print(f"It will be a tough winter! More {floor(abs(litres_wine_result))} liters wine needed.")
else:
    litres_wine_per_worker = litres_wine_result / number_of_workers
    print(f"Good harvest this year! Total wine: {floor(litres_wine_produced)} liters.")
    print(f"{ceil(litres_wine_result)} liters left -> {ceil(litres_wine_per_worker)} liters per person.")
