words = "navgurukul is great "
# words=input("enter the though")
a=[]
string=""
for i in words:
    if i==" ":
        a.append(string)
        string=""
    else:
        string+=i
if string:
    a.append(string)
print(a)
