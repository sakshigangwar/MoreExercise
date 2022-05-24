# list1 = [1, 5, 10, 12, 16, 20]
# list2 = [1, 2, 10, 13, 16]
# a=[]
# i=0
# while i<len(list1):
#     if list1[i] in list2:
#         a.append(list1[i])
#     else:
#         a.append(list1[i])
#     i=i+1
# print(a)

# o/p=new_list = [1, 2, 5, 10, 12, 13, 16, 20]

list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
a=[]
i=0
j=0
while i<len(list2):
    list1.append(list2[i])
    while j<len(list1):
        if list1[j] not in a:
            a.append(list1[j])
        j+=1
    i=i+1
print(a)



