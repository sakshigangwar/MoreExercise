# num=int(input("enter the number :"))
# i=num
# sum=0
# while (i>0):
#     k=i%10
#     i=i//10
#     sum+=k
# if num%sum==0:
#     print(num,"true")
# else:
#     print(num,"false") 

num=int(input("enter the number :"))
i=0
sum=0
while i>num:
    sum=sum+(i%10)
    i=i//10
if num%sum==0:
    print("harshad")
else:
    ("not harshad")


