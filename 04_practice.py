# x=input("Enter the name : ")
# y=input("Enter the DATE : ")
# a=a.replace("< DATE >",y)
# a=a.replace("< NAME >",x)

# print(a.find("  "))
# print(a.replace("  "," "))

# print(x.endswith("an"))
# print(x.capitalize()) 
# print(x.find("u"))
# print(\"this is great"\ )


# a1=input("Enter the marks1 : ")
# a2=input("Enter the marks2 : ")
# a3=input("Enter the marks 3: ")
# a4=input("Enter the marks 4: ")
# a5=input("Enter the marks 5: ")
# a6=input("Enter the marks 6: ")
# a7=input("Enter the marks 7: ")
# a=[a1,a2,a3,a4,a5,a6,a7]
# a.sort()
# print(a)
# a={
#     "name":"aneeq",
#     "marks": "1038",}

# print(a['marks'])
# a=set()
# a.add(5)
# a.add((25,5,69,45))
# # print(a)
# # print(len(a))
# # a.remove(5)
# # print(a)
# # print(a.pop())
# # print(a.clear())
# print(a.union({2}))
# print(a.intersection({5}))
# # 
# a='''  DEAR  : < NAME >
#                  You are selected!
#        DATE  :     < DATE >
#            '''
# x=input("Enter the name : ")
# y=input("Enter the DATE : ")
# a=a.replace("< DATE >",y)
# a=a.replace("< NAME >",x)
# print(a)
# print(x.endswith("an"))
# print(x.capitalize()) 
# print(x.find("u"))

# a={
#     "pani":"water",
#     "khana":"food"
# }
# print("options are",a.keys())
# b=input("Enter the word : ")
# print("the meaning of word is : ",a[b])
# a1=input("Enter the number : ")
# a2=input("Enter the number : ")
# a3=input("Enter the number : ")
# a4=input("Enter the number : ")
# a5=input("Enter the number : ")
# a6=input("Enter the number : ")
# a7=input("Enter the number : ")
# a8=input("Enter the number : ")
# b=set()
# b.add(a1)
# b.add(a2)
# b.add(a3)
# b.add(a4)
# b.add(a5)
# b.add(a6)
# b.add(a7)
# b.add(a8)
# print(b)
# a={"18",18}
# print(a)
# a=set()
# a.add(22)
# a.add(22.)
# a.add("22")
# print(len(a))
# a={}
# print(type(a))
# a={
#     '''aneeq
#     '''
# }
# a=float(input("Enter n1 : "))
# b=float(input("Enter n2 : "))
# c=float(input("Enter n3 : "))
# d=float(input("Enter n4 : "))
# if(a>b and a>c and a>d ):
#      print("n1 is greater")
# elif(b>a and b>c and b>d ): 
#      print("n2 is greater")
# a=float(input("Enter n1 : "))
# b=float(input("Enter n2 : "))
# c=float(input("Enter n3 : "))
# d=float(input("Enter n4 : "))
# sn1=a/100*100
# sn2=b/100*100
# sn3=c/100*100
# sn4=d/100*100
# tn=a+b+c+d
# tnper=tn/400*100
# if(sn1>=33 and sn2>=33 and sn3>=33 and sn4>=33 and tnper>=40):
#      print("pass")     
# else:
#      print("fail")  
# a=input("Enter the name : ")
# if(len(a)>10):
#      print("yes")   
# a=["aniq","coder","start",25,"coder"]
# b=input("Enter : ")
# if(b in a):
#      print("yes")
# i=0
# while i<len(a):
#      print(a[i])
#      i=i+1
# for items in a: 
#      print(items)
# print(4%2)
# a=int(input("Enter the num to CHECK the # is PRIME OR NOT : "))
# for i in range(2,101):
#      for f in range(1,i):
#          if(f!=1 and i%f==0):
#              flag=0
#              if(flag!=0):   
#                print(i)
#          else:
#             print(str(i)+"  is a Prime Number")
# if(flag==0):
# #     print("Prime Number")
# # else:
# #     print("Not a Prime Number")
# # print("itne bare hogaye ho abhi tak ye nhi pata ke prime num kya hote ha.PROGRAM use kar rahe hu. ")
# # a=int(input("gfg"))
# # print(,a)
# minimum = int(input(" Please Enter the Minimum Value: "))
# maximum = int(input(" Please Enter the Maximum Value: "))

# for Number in range (minimum, maximum + 1):
#     count = 0
#     for i in range(2, (Number//2 + 1)):
#         if(Number % i == 0):
#             count = count + 1
#             break

#     if (count == 0 and Number != 1):
#         print("Prime NUM :",Number)
# print('Prime numbers between 1 and 100 are:')
# min = int(input(" Please Enter the Minimum Value: "))
# max = int(input(" Please Enter the Maximum Value: "))

# for num in range(min,max+1):
#    if num > 1:
#        for i in range(2,num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)
# vegitables = ['Cabbage' , 'Carrot ','Beans', 'Corn'] #create a list and store 4 items
# print(vegitables) #print values
# # vegitables.append('mushroom') #append is function to add values in list
# # print(vegitables)
# vegitables.insert(2)
# print(vegitables)
# # a=[5,2,9,7]
# # a.pop(2)
# # print(a)
# tuple4 = (1) #[WRONG TUPLE IT'S GENERATE AN ERROR]
# print(tuple4)
# for i in range(0,3):
# #         print("*" * 2)
# for i in range(1,3)
#         print
# def table(n):
#         for i in range(1,11):
#                 print(f"{n} x {i} = {i*n}")
#         pass


# a=int(input("Enter the number whose table did you want"))
# b=table(a)
# print(b)
# f=open('01_Hello.py' , 'r')
# # data=f.read()
# data=f.readline() #only read one line of file
# print(data)
from colorama import Fore
print(Fore.RED + "Helllo World")


