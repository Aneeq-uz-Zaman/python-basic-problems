a=input("Enter operation +,-,*,/ : ")
b=float(input("Enter the first value : "))
c=float(input("Enter the second value : "))
# b=float(b)
# c=float(c)
if(a=="+"):
    print("You Enter operation '+'")
    print("Answer is : ",b+c)
elif(a=="-"):
     print("Answer is : ",b+c)
elif(a=="*"):
     print("Answer is : ",b*c)
elif(a=="/"):
    print("Answer is : ",b/c)
else:
     print("Wrong Operation")
