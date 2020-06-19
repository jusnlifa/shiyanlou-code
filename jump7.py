for n in range(1,101):
    s=str(n)
    if(n%7==0 or s.count('7')):
        continue
    print(n)
