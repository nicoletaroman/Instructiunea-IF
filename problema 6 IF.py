n1=int(input("dati un nr")) 
n2=int(input("dati un nr"))
n3=int(input("dati un nr"))
if n3>=8:
    print(n1," ",n2," ",n3)
if n3<8:
    if n1>n2:
        print(n1)
    else:
        print(n2)
if n1>10 or n2>10 or n3>10:
    print("nu este asa nota")