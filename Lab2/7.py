def election(x:int,y:int,z:int)->int:
    s=x+y+z
    if s>=2:
        return 1
    return 0

a,b,c=map(int,input().split())
print(election(a,b,c))