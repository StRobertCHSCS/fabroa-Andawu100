'''
-------------------------------------------------------------------------------
Name:		Livehack2problem.py
Purpose:	Determine the type of triangle with the given angles

Author:	Chester.A

Created:	18/11/2019
------------------------------------------------------------------------------
'''
#Welcoming to the program
print("Welcome to the Triangle Checker")
#Get angle values
a1 = int(input("Enter the first angle: "))
a2 = int(input("Enter the second angle: "))
a3 = int(input("Enter the third angle: "))

#Determine the type of triangle
if a1 == a2 == a3 == 60:
    print("The triangle with angles ", a1, ",", a2, "and " , a3 ,
          "forms an Equilateral triangle.")

elif a1 == a2 and a1 + a2 + a3 == 180:
    print("The triangle with angles", a1, ",", a2, "and ", a3 , "forms and Isosceles triangle.")

elif a1 == a3 and a1 + a2 + a3 == 180:
    print("The triangle with angles", a1, ",", a2, "and ", a3 , "forms and Isosceles triangle.")

elif a2 == a3 and a1 + a2 + a3 == 180:
    print("The triangle with angles", a1, ",", a2, "and ", a3 , "forms and Isosceles triangle.")

elif a1 + a2 + a3 == ("180"):
    print("The triangle with angles"+ a1 + a2, "and " + a3 , "forms and scalene triangle.")

else:
    print("Error, the angles do not form a triangle.")