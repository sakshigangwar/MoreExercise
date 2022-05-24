# # string ki lenth

# string_name = "Shakrudin"
# print (len(string_name))


# # in use krna h ki wo item h ya ni 

# string_name = "navgurukul"
# if "n" in string_name:
#     print ("n hai")
# else:
#     print ("n nahi hai")

# print("creat password")
# ch=input("enter the alpha")
# if ch>"a" or ch>="A" and ch<="z" or ch<="Z":
#     digit=str(input("enter the number"))
#     if digit>="1" and digit<="9":
#         sc=input("enter special charecter")
#         if  sc=="@" or sc=="#" or sc=="&" or sc=="*":
#             a=(ch+sc+str(digit))
#             if len(a)>=8 or len(a)<16:
#                 print("strong password")
#             else:
#                 print("not strong password")
#         else:
#             print("this is not strong password")
#             print("please creat strong password")
#     else:
#         print("invalid")
# else:
#     print("something wrong")


s=5
i=1
while i<=5:
    j=1
    while j<=5:
        if j<i:
            print(i,end="")
        else:
            print(j,end="")
        j=j+1
    print()
    s=s+5
    i=i+1



# s=5
# i=1
# while i<5:
#     j=1
#     while j<5:
#         if j<i:
#             print(i,end=" ")
#         else:
#             print(j,end=" ")
#         j=j+1
#     print()
#     s=s+1
#     i=i+1





