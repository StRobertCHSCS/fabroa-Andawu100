'''

-------------------------------------------------------------------------------
Name:     problem2.py
Purpose:  determaning how many pieces of chicken mr fabroa and his class get

Author:   chester.Andrew

Created:  02/10/2019
-------------------------------------------------------------------------------
'''

# find how many pieces of chicken there are
chicken = int(input("How many pieces of chicken are there?  "))

# divide the chicken between the students(22) and give mr fabroa the remanders.
students = chicken // 22
fabroa = chicken % 22

# output the amount of chicken everyone gets.
print("Each student will get ", students, "piece(s) of chicken and"
      " Mr. Fabroa will get ", fabroa, "piece(s) of chicken.")
