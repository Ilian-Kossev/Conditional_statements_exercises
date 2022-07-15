from math import floor

hours_needed = int(input())
project_days = int(input())
number_of_workers_overtime = int(input())
work_days = project_days * 0.9
project_hours_regular_time = work_days * 8
project_hours_overtime = project_days * 2 * number_of_workers_overtime
total_work_hours = project_hours_regular_time + project_hours_overtime
hour_difference = total_work_hours - hours_needed
if total_work_hours >= hours_needed:
    print(f"Yes!{floor(hour_difference)} hours left.")
else:
    print(f"Not enough time!{abs(floor(hour_difference))} hours needed.")
