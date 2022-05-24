from email import message


choice=input("what do you want do do?\n1.encrypet a message,2.decrypet a message\n")
if choice=="e":
    print("encrypet")
elif choice=="d":
    print("decrypet")
def encrypet():
    message=input("enter the message you want to encrypet")
    ascii_message=[ord(char)+3 for char in message ]
    encrypet_message=[chr(char)for char in ascii_message]
    print(''.join(encrypet_message))
def decrypet():
    message=input("enter the message you want to decrypet")
    ascii_message=[ord(char)-3 for char in message]
    decrypet_message=[chr(char)for char in ascii_message]
    print(''.join(decrypet_message))
encrypet()
decrypet()




# chars =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']
# chars[13]="n"
# shifted_chars[13]="p"
# chars[0]="a"
# shifted_chars[0]="c"
# print(chars)
# print(shifted_chars)
