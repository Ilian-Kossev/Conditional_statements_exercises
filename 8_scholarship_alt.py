income = float(input())
average_grade = float(input())
min_salary = float(input())
social_scholarship = int(min_salary * 0.35)
excellent_scholarship = int(average_grade * 25)
if average_grade >= 5.50:
    if income > min_salary:
        print(f"You get a scholarship for excellent results {excellent_scholarship} BGN")
    else:
        if excellent_scholarship >= social_scholarship:
            print(f"You get a scholarship for excellent results {excellent_scholarship} BGN")
        else:
            print(f"You get a Social scholarship {social_scholarship} BGN")
elif average_grade > 4.50:
    if income < min_salary:
        print(f"You get a Social scholarship {social_scholarship} BGN")
    else:
        print(f"You cannot get a scholarship!")
else:
    print(f"You cannot get a scholarship!")