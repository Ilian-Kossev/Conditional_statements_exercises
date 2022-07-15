from math import floor
record_time = float(input())
distance_in_metres = float(input())
one_meter_swimming_time_in_seconds = float(input())
delay = distance_in_metres // 15 * 12.5
new_time = distance_in_metres * one_meter_swimming_time_in_seconds + delay
if new_time < record_time:
    print(f"Yes, he succeeded! The new world record is {new_time:.2f} seconds.")
else:
    difference = new_time - record_time
    print(f"No, he failed! He was {difference:.2f} seconds slower.")
