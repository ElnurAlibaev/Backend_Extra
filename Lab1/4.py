x=int(input())
h=x*45
h+=(x//2-1+x%2)*15
h+=((x+1)//2-1+(x+1)%2)*5
print(h//60+9,h%60)