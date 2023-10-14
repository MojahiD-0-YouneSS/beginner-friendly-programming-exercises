import sys
#If the average score is 7 and above print "Good job!", 
#if the average score is between 6 and 4 print "You need to work harder!", 
#if the average score is below 4 print "Failed, you really need to work harder!".

geo_grade = int(input("enter your Geometry grades :"))
alg_grade = int(input("enter your Algebra grades :"))
phs_grade = int(input("enter your Physics grades :"))
def chek_range(geo_grade, alg_grade, phs_grade):
    i = 0
    if  geo_grade  in  range(1, 11) and alg_grade in range(1, 11) and phs_grade in range(1, 11):
            pass
    else:
            print("Erreur : grade not in valid range , please enter a valid grade")
            sys.exit()
chek_range(geo_grade, alg_grade, phs_grade)

def Calculate_averg_grade (geo_grade, alg_grade, phs_grade):
    average = int((geo_grade + alg_grade + phs_grade)/3)
    if average >= 7:
        print("Good job!")
    elif average in range(4,7):
        print("You need to work harder!")
    else:
         print("Failed, you really need to work harder!")
    return average
print(Calculate_averg_grade(geo_grade, alg_grade, phs_grade))




