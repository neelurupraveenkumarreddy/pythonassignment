#to find year is a leap year or not
m=int(input("enter a year"))
if (m%4==0 and m%100!=0 or m%400==0):
    print("m is aleap year")
else:
    print("m is not a leap year")
