# # # # # # # # for print integer division:
# # # # # # # #           print(a//b)
# # # # # # # # for print floast division:
# # # # # # #                 #   print(a//b)

# # # # # # # def number(x):
# # # # # # #     for i in range(1,x):
# # # # # # #         print(i)
# # # # # # #         for j in range(0,i):
# # # # # # #            a=[]
# # # # # # #            a.append(j)
# # # # # # #     return a
# # # # # # # n = int(input("sf"))
# # # # # # # print(number(n))
# # # # # # # int(input().strip())
# # # # # # a=[]
# # # # # # a=int(int(input("hi")))
# # # # # n=int(input("Enter number of element in list : "))
# # # # # a=[]

# # # # # for i in range(0,n):
# # # # #     b=int(input("Enter Element of List :  "))
# # # # #     a.append(b)
    
# # # # # print(a)    
# # # # # a.sort()
# # # # # a.reverse()
# # # # # print(a[1])
# # # # def find_runner_up(scores):
# # # #     scores = set(scores)
# # # #     scores = sorted(scores, reverse=True)
   
# # # #     return scores[1]   

# # # # n=int(input("Enter number of element in list : "))
# # # # scores = []
# # # # for i in range(0,n):
# # # #     score=int(input("Enter Element of List :  "))
# # # #     scores.append(score)

# # # # runner_up_score = find_runner_up(scores)
# # # # print("The runner-up score is:", runner_up_score)
# # # # scores=[8,9,8,7,9]
# # # list1=[]
# # # N=int(input("Enter the number of element do you insert : "))
# # # for i in range(0,N):
# # #     a=int(input("Enter the element  : "))
# # #     list1.insert(i,a)
# # # list1.append(list1[0])
# # # print(list1)    
# # # print(list1)
# # # list1.remove(list1[0])
# # # print(list1)
# # # list1.append(list1[0])
# # # print(list1)
# # # list1.sort()
# # # print(list1)
# # # list1.pop(N-1)
# # # print(list1)
# # # list1.reverse()    
# # # print(list1)
# # # # print(scores)
# # # cmd = input().split()

# # first_name = input("Enter fisrt name : ")
# # last_name = input("Enter Last name : ")
# # print(first_name, last_name)
# # print(f"Hello {first_name} {last_name}")
# def find_runner_up(scores):
#     scores = set(scores)
#     scores = sorted(scores, reverse=True)
#     return scores[1]   

# n=int(input())
# scores = []
# for i in range(0,n):
#     score=int(input())
#     scores.append(score)

# runner_up_score = find_runner_up(scores)
# print("The runner-up score is:", runner_up_score)
N=int(input("Enter # of Students : "))
name=[[0,0],[0,0]]
score=[]
for i in range(0,N):
      a=input("Enter the name : ")
      name[i][0]=a
      b= input('Enter the number : ')
      name[i][1]=a
print(name)    
# a=[['aniq','91'],['aman','92']]
# print(a[0][1])