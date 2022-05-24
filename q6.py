# remove duplicate

list=["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
i=0
b=[]
while i<len(list):
    if list[i] not in b:
        b.append(list[i])
    i=i+1
print(b)
