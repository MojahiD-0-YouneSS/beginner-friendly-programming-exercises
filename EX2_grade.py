geo_grade = int(input("enter your Geometry grades :"))
alg_grade = int(input("enter your Algebra grades :"))
phs_grade = int(input("enter your Physics grades :"))
def chek_range(geo_grade, alg_grade, phs_grade):
    i = 0
    if  geo_grade  in  range(1, 11) and alg_grade in range(1, 11) and phs_grade in range(1, 11):
            pass
    else:
            print("Erreur : grade not in valid range !")
            print("Erreur : please enter a valid grade")
chek_range(geo_grade, alg_grade, phs_grade)

def Calculate_averg_grade (geo_grade, alg_grade, phs_grade):
    average = int((geo_grade + alg_grade + phs_grade)/3)
    if average == 5:
        print("not bad!")
    elif average > 5:
        print("nice grade!")
    else:
         print("do more work!")
    return average
print(Calculate_averg_grade(geo_grade, alg_grade, phs_grade))