
# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))

'''
>>Output/Runtime Test Cases:
     
Enter value in kilometers: 2.5
3.50 kilometers is equal to 1.55 miles
'''
