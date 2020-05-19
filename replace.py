plaincode=input()
for p in plaincode:
    if ord("a")<=ord(p)<=ord("z"):
        print(chr(ord(p)+26),end='')
    elif ord("A")<=ord(p)<=ord("Z"):
        print(chr(ord(p)+26),end='')
    else:
        print(p,end='')
