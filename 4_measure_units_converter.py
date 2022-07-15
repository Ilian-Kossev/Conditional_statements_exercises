number = float(input())
measure_1 = input()
measure_2 = input()
result = 0
if measure_1 == "mm" and measure_2 == "cm":
    result = number / 10
elif measure_1 == "mm" and measure_2 == "m":
    result = number / 1000
elif measure_1 == "cm" and measure_2 == "mm":
    result = number * 10
elif measure_1 == "cm" and measure_2 == "m":
    result = number / 100
elif measure_1 == "m" and measure_2 == "mm":
    result = number * 1000
elif measure_1 == "m" and measure_2 == "cm":
    result = number * 100
print(f"{result:.3f}")
