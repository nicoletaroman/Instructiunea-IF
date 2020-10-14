a=int(input("dati un nr"))
b=int(input("dati un nr"))
if a%2==0 and b%2==0:
    if a>b:
        print (a)
    else:
        print(b)
if a%2==0 and b%2!=0:
    print(a)
if a%2!=0 and b%2==0:
    print(b)
if a%2!=0 and b%2!=0:
    print("nu sunt nr pare")