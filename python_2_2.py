length=float(input("How tall are you?\n"))
weight=float(input("What's your weight ?\n"))
bulk=(weight/(length*length))
if bulk>24.5 or bulk <18.5 :
    print(f"you are not on shape")
else :
    print( f"you are in good mood")
