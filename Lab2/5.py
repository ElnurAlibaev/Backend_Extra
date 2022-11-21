x=input()
ans=0
for i in range(len(x)):
    ans+=(int(x[i])*(2**(len(x)-1-i)))
print(ans)