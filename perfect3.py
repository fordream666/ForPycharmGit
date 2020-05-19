import math
Num = int(input())
for a in range(2,Num+1):
    for b in range(2,a):
        for c in range(b,a):
            for d in range(c,a):
                if math.pow(a,3) == math.pow(b,3)+math.pow(c,3)+math.pow(d,3):
                    print("Cube = %d,Tripe = (%d,%d,%d)" %(a,b,c,d))
