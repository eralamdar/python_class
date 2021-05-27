nn=float(input("please enter first number\n"))
mm=float(input("please enter second number\n"))
o=(input("pleae enter your operation\n"))
if o=="+":
    print(f"{nn}+{mm}={nn+mm}\n")
elif o=="*":
    print(f"{nn}*{mm}={nn*mm}\n")
elif o=="/":
    print(f"{nn}/{mm}={nn/mm}\n")
elif o=="-":
    print(f"{nn}-{mm}={nn-mm}\n")
elif o=="**":
    print(f"{nn}**{mm}={nn**mm}\n")
else:
    (print(f" Man balad nistam"))
