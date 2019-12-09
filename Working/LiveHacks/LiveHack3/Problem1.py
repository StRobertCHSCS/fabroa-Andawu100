'''
-------------------------------------------------------------------------------
Name: practice1.py
Purpose: Calculate the total amount of heating days

Author: Andrew Chester

Created: date 09/12/2019
-------------------------------------------------------------------------------
'''
#Find the amount of days to count
print("******  Heating Days Tracker ******")
days = int(input("Enter the number of days: "))
heat = 0

#Get user input for the temperatures, calculate the amount of values above 15
while days > 0:
    temps = int(input(""))
    days = days - 1
    if temps < 15:
        heat += 1
#print the total numbers of heating days
print("There are", heat ,"heating days.")



