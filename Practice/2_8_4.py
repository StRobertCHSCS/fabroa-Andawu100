#Find the value of the numbers
start = int(input("Enter the first number: "))
end = int(input("Enter the second number: "))



#compute the total from 1 to number

if start < end:
    for i in range(start, end+1):        
        print(i)

else:
    for i in range(end, start, -1):
        print(i)
