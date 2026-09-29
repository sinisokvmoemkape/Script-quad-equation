a = float(input("enter a: "))
b = float(input("enter b: "))
c = float(input("enter c: "))

deskriminant = (b**2)-(4*a*c)
print(f"deskriminant raven {deskriminant}")
if deskriminant < 0:
    print("lahendused puuduvad")
elif deskriminant > 0:
    x1 = (-b+deskriminant**(1/2))/(2*a)    
    x2 = (-b-deskriminant**(1/2))/(2*a)
    print(x1, "\n", x2)
else:
    x1 = -b/(2*a)
    print(x1)