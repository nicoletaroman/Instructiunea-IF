a=int(input("dati un nr"))
b=int(input("dati un nr"))
c=int(input("dati un nr"))
if a>=0 and b>=0 and c>=0:
    if b>c:
        print(b)
    else:
        print(c)
if a<0 or b<0 or c<0:
    print(a+b)