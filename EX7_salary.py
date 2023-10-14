years_employed = int(input("Enter your years of employmnt : "))
number_children = int(input("Enter your years of employmnt : "))
minimum_wage = 400
def calculate_amount_salary(years_employed, number_children, minimum_wage) :
    total_salary = minimum_wage + 20 * years_employed + 30 * number_children
    years_experience = 20 * years_employed
    child_salary = 30 * number_children
    return f"The total amount is {total_salary}$. 400$ minimum wage + {years_experience}$ for {years_employed} years experience + {child_salary}$ for {number_children} kids"

print(calculate_amount_salary(years_employed, number_children, minimum_wage))