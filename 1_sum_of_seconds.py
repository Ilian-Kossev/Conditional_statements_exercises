time_first = int(input())
time_second = int(input())
time_third = int(input())
total_time = time_first + time_second + time_third
hours = total_time // 60
minutes = total_time % 60
print(f"{hours}:{minutes:0>2d}")

#alt:
#time_first = int(input())
#time_second = int(input())
#time_third = int(input())
#total_time = time_first + time_second + time_third
#hours = total_time // 60
#minutes = total_time % 60
#if minutes < 10:
#    print(f"{hours}:0{minutes}")
#else:
#    print(f"{hours}:{minutes}")