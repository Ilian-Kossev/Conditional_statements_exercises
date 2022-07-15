number = int(input())
bonus_points = 0
even_number_bonus_points = 0
ending_number_bonus_points = 0
if number <= 100:
    bonus_points = 5
elif 100 < number <= 1000:
    bonus_points = number * 0.2
else:
    bonus_points = number * 0.1
if number % 2 == 0:
    even_number_bonus_points = 1
elif number % 10 == 5:
    ending_number_bonus_points = 2
total_bonus_points = bonus_points + even_number_bonus_points + ending_number_bonus_points
total_sum = number + total_bonus_points
print(total_bonus_points)
print(total_sum)
