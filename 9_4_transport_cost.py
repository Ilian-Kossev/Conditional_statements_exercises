distance = int(input())
time_of_day = input()
price_bus = distance * 0.09
price_train = distance * 0.06
price_taxi = 0
price_transport = 0
if time_of_day == "day":
    price_taxi = 0.7 + 0.79 * distance
elif time_of_day == "night":
    price_taxi = 0.7 + 0.9 * distance
if distance < 20:
    price_transport = price_taxi
elif 20 <= distance < 100:
    price_transport = price_bus
else:
    price_transport = price_train
print(f"{price_transport:.2f}")
