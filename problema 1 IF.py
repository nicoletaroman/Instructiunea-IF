n1=int(input("dati nr curent"))
p1=int(input("dati punctajul"))
n2=int(input("dati nr curent"))
p2=int(input("dati punctajul"))
n3=int(input("dati nr curent"))
p3=int(input("dati punctajul"))
if p1>p2 and p1>p3:
    print("punctajul maxim are elevul cu nr" ,n1)
if p2>p1 and p2>p3:
    print("punctajul maxim are elevul cu nr",n2)
if p3>p1 and p3>p2:
    print("punctajul maxim are elevul cu nr",n3)