def count_u_l(s):
    u=0
    l=0
    for i in s:
        if i.isupper():
            u+=1
        elif i.islower():
            l+=1
        else:
            continue
    print("No.of Upper case characters :",u)
    print("No.of Lower case characters :",l)
    
s=input("enter a string")
count_u_l(s)