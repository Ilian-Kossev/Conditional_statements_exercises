from math import floor

income = float(input())
grade = float(input())
minimum_salary = float(input())
social_scholarship = 0
excellent_grade_scholarship = 0
eligible_for_social_scholarship = False
eligible_for_grade_scholarship = False
if grade > 4.5 and income < minimum_salary:
    social_scholarship = minimum_salary * 0.35
    eligible_for_social_scholarship = True
if grade >= 5.5:
    excellent_grade_scholarship = grade * 25
    eligible_for_grade_scholarship = True
if not eligible_for_social_scholarship and not eligible_for_grade_scholarship:
    print(f"You cannot get a scholarship!")
elif eligible_for_social_scholarship and not eligible_for_grade_scholarship:
    print(f"You get a Social scholarship {floor(social_scholarship)} BGN")
elif eligible_for_grade_scholarship and not eligible_for_social_scholarship:
    print(f"You get a scholarship for excellent results {floor(excellent_grade_scholarship)} BGN")
elif eligible_for_social_scholarship and eligible_for_grade_scholarship:
    if excellent_grade_scholarship >= social_scholarship:
        print(f"You get a scholarship for excellent results {floor(excellent_grade_scholarship)} BGN")
    else:
        print(f"You get a Social scholarship {floor(social_scholarship)} BGN")



