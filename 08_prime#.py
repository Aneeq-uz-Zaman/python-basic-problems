from ast import Num


print(" PROGRAM To CHECK the numbers are PRIME or NOT  ")
x=int(input("Enter 1 for check one number & 2 for check prime numbers between two numbers  "))

if(x==1):
    a=int(input("Enter the num to CHECK the # is PRIME OR NOT : "))
    for f in range(2,a):
               if( a%f==0):
                    flag=1
                    break
               else:
                    flag=0
    if(flag==0):
          print("Prime Number")
    else:
          print("Not a Prime Number")

elif(x==2):
     min = int(input(" Please Enter the Minimum Value: "))
     max = int(input(" Please Enter the Maximum Value: "))
     for num in range(min,max):
        #   if num > 1:
               for i in range(2,num):
                  if (num % i and num>1) == 0:
                          break
               else:
                       print("PRIME NUMBER : ",num)
else:
    print("YOU ENTER WRONG INTEGER")
    print("Enter  1 for check one num & 2 for range ")
   
