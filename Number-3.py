import time
import sys

print("==================================================")
print("Please enter your data below:")
print("==================================================")
Newly_Hired_Male = int(input("Enter the number of male newly hired employees: "))
Newly_Hired_Female = int(input("Enter the number of female newly hired employees: "))
Permanent_Male = int(input("Enter the number of male permanent employees: "))
Permanent_Female = int(input("Enter the number of female permanent employees: "))
Resigned_Male = int(input("Enter the number of male resigned employees: "))
Resigned_Female = int(input("Enter the number of female resigned employees: "))


Total_Newhires = Newly_Hired_Male  + Newly_Hired_Female
Total_Permanent = Permanent_Male + Permanent_Female
Total_Resigned = Resigned_Male + Resigned_Female
Total_Employees = Total_Newhires + Total_Permanent


Percentage_Male_New_Hires = (Newly_Hired_Male  / Total_Newhires) * 100
Percentage_Female_New_Hires = (Newly_Hired_Female / Total_Newhires) * 100
Percentage_Male_Permanent = (Permanent_Male / Total_Permanent) * 100
Percentage_Female_Permanent = (Permanent_Female / Total_Permanent) * 100
Percentage_Male_Resigned = (Resigned_Male / Total_Resigned) * 100
Percentage_female_Resigned = (Resigned_Female / Total_Resigned) * 100

print("\nPlease wait", end="")

for i in range(8):
    time.sleep(.5)
    sys.stdout.write('.')
    sys.stdout.flush()

print("\nThank you for the waiting! \nPlease see the summary below:")

print("\n=================R E S U L T S=================")
print("\nTotal number of newly hired employees: ", Total_Newhires)
print("Percentage of male new hires: %.2f"%Percentage_Male_New_Hires)
print("Percentage of female new hires: %.2f"%Percentage_Female_New_Hires)

print("\nTotal number of permanent employees: ", Total_Permanent)
print("Percentage of male permanent employees: %.2f"%Percentage_Male_Permanent)
print("Percentage of female permanent employees: %.2f"%Percentage_Female_Permanent)

print("\nTotal number of resigned employees: ", Total_Resigned)
print("Percentage of male resigned employees: %.2f"%Percentage_Male_Resigned)
print("Percentage of female resigned employees: %.2f"%Percentage_female_Resigned)

print("\n==================================================")
print("Total number of employees: ", Total_Employees)
print("Total number of resigned employees: ", Total_Resigned)
print("==================================================")
print("\n\nTHANK YOU AND HAVE A GREAT DAY!")
