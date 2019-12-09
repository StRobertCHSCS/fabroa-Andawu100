'''
-------------------------------------------------------------------------------
Name: practice2.py
Purpose: 

Author: Andrew Chester

Created: date 09/12/2019
-------------------------------------------------------------------------------
'''
#Intitlize the variables
print(" ***** Welcome to the Distance Tracker ******")
total = 0
days = 0

#get the user inputs
while total < 100:
   dis = int(input("Enter the distance traveled for today: "))
   total = total + dis
   days = days + 1

#find the average
avg = total/days

#print out the amount of days taken and the average distance driven
print("It took", days, "days to surpass 100km driven.")
print("The average distance driven per day is", avg, "km.")
