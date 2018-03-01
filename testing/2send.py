file = open("testfile.txt","w")
for _ in range(int(input())):
    a=0
    b=0
    ma=0
    mb=0
    for s in range(int(input())):
        p,q = map(int,input().split())
        if p>q:
            a+=1
        elif q>p:
            b+=1
        mb=max(q,mb)
        ma=max(p,ma)
    # print (a,b)
    if a>b:
        file.write("1 ")
        file.write(str(ma))
    elif b>a:
        file.write("2 ")
        file.write(str(mb))
    else:
        file.write("draw")
    file.write("\n")

file.close()