years_employed = int(input("Enter your years of employmnt : "))
number_children = int(input("Enter your yearsnumber of children : "))
number_days_missed = int(input("Enter your missing days : "))

minimum_wage = 400
def salaru_days(number_days_missed):
    if number_days_missed == 0:
        return 1
    else:
        return 0
def calculate_amount_salary(years_employed, number_children, minimum_wage, number_days_missed) :
    number_days_salary = salaru_days(number_days_missed) * 100
    years_experience = 20 * years_employed
    child_salary = 30 * number_children
    total_salary = minimum_wage + 20 * years_employed + 30 * number_children + number_days_salary
    return f"The total amount is {total_salary}$, 400$ minimum wage + {years_experience}$ for {years_employed} years experience + {child_salary}$ for {number_children} kids + {number_days_salary}$ for {number_days_missed} missing a day at work"

print(calculate_amount_salary(years_employed, number_children, minimum_wage, number_days_missed))