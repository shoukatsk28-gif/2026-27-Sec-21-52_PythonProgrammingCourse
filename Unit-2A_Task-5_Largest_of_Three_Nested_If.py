x=int(input("enter first number:"))
y=int(input("enter second number:"))
z=int(input("enter third number:"))

if x>=y :
    if x>z:
        largest=x
    else:
        largest=z


        if y>z:
            largest=y
        else:
            largest=z
            print(f"largest={largest} (among{x},{y},{z})")