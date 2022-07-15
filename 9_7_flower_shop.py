from math import floor, ceil

number_magnolias = int(input())
number_zjumbjuls = int(input())
number_roses = int(input())
number_cacti = int(input())
present_price = float(input())
price_magnolias = number_magnolias * 3.25
price_zjumbjuls = number_zjumbjuls * 4
price_roses = number_roses * 3.5
price_cacti = number_cacti * 8
total_price_after_taxes = (price_magnolias + price_zjumbjuls + price_roses + price_cacti) * 0.95
difference = present_price - total_price_after_taxes
if difference <= 0:
    print(f"She is left with {floor(abs(difference))} leva.")
else:
    print(f"She will have to borrow {ceil(difference)} leva.")