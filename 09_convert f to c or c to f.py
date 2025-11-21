a=int(input("press 1 for C to F OR press 2 for F to C: "))
if(a==1):
    b = float(input("Enter the temperature in celsius : "))
    b=  (b*9/5)+32
    print(str(b)+" F")
elif(a==2):
    c=float(input("Enter the temperature in faranheit : "))
    c=(c-32)*5/9
    print(str(c)+"C")
else:
     print("Entering wrong number")
# def cel(temp):
#     return (temp-32)*5/9
# a=float(input("Enter Temperature in Farhanheit : "))
# print(cel(a))