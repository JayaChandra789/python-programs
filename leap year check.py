#Program to print leap year or not
def leap_year_verify(year):
 if (year%400== 0) or (year%4==0 and year%100!=0):
   return "True"
 else:
   return "False"

year=int(input("Enter year: "))
result=leap_year_verify(year)
print(result)
if result=="True":
 print("Entered year  is leap year")
else:
 print("Entered year  is not leap year")

