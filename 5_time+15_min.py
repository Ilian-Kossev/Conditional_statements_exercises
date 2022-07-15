hours = int(input())
minutes = int(input())
total_minutes = hours * 60 + minutes + 15
real_hours = total_minutes // 60
real_minutes = total_minutes % 60
if real_hours >= 24:
    real_hours %= 24      # with %= is valid for any number of minutes
print(f"{real_hours}:{real_minutes:0>02d}")