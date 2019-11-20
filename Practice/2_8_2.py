#Find the value of number
number = int(input("Enter a number: "))

#initialize the total

total = 0

#compute the total from 1 to number
''' 
The third digit (2) changes it to only output odd numbers
'''
for i in range(1,number+1, 2):
    print(i)
    total = total + i

#total output
print(total)