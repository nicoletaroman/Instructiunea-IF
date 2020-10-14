ac=int(input("dati anul curent"))
lc=int(input("dati luna curenta"))
zc=int(input("dati ziua curenta"))
an=int(input("dati anul nasterii"))
ln=int(input("dati luna nasterii"))
zn=int(input("dati ziua curenta"))
if ln>lc:
    print (ac-an-1,"ani")
if ln==lc:
    if zn>zc:
        print(ac-an-1,"ani")
    if zn<zc:
        print(ac-an,"ani")
    if zn==zc:
        print(ac-an,"ani")
else:
    print(ac-an,"ani")