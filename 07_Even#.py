print("PROGRAM TO CHECK THE NUMBERS ARE EVEN OR ODD   ")
x=int(input("Enter 1 for check one number & 2 for check EVEN OR ODD NUMBERS between two numbers : "))
if(x==1):
    y=int(input("Enter the number : "))
    if(y%2==0):
           print(str(y)  +  "  " + "is EVEN")
    else:
        print(str(y) +  "  " +  "is ODD") 
elif(x==2):
     a=int(input("Enter the 1st num of range to find #s is odd or even : "))
     b=int(input("Enter the last num of range to find #s is odd or even : "))
     for f in range(a,b):
       if(f%2==0):
           print(str(f)  +  "  " + "is EVEN")
       else:
        print(str(f) +  "  " +  "is ODD")    
    
    

    