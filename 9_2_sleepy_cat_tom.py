number_days_off = int(input())
workdays = 365 - number_days_off
playminutes = workdays * 63 + number_days_off * 127
if playminutes >= 30000:
    minutes_overplay = playminutes - 30000
    hours = minutes_overplay // 60
    minutes = minutes_overplay % 60
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    minutes_left_for_play = 30000 - playminutes
    hours = minutes_left_for_play // 60
    minutes = minutes_left_for_play % 60
    print(f"Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")



