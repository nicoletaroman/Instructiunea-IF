ng=int(input("dati nr de gaini"))
nb=int(input("dati nr de boabe"))
t=nb//ng
m=nb-t*ng
if nb-t*ng==t:
    print("egalitate,primesc cate ",t,"boabe")
if nb-t*ng>t:
    print("curcanul primeste cu",m-t,"boabe mai mult")
if nb-t*ng<t:
    print("curcanul primeste cu",t-m,"boabe mai putin")