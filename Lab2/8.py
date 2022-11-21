def add_money(m:float, x:float)->float:
    m+=x
    return m

def remove_money(m:float, x:float)->float:
    m-=x
    return m

def recount_money(m:float, c:str):
    if c=="tenge":
        c="dollars"
        m=m/464
    else:
        c="tenge"
        m=m*464

money=4640.0
currency="tenge"

money=add_money(money,464.0)
print(money)

money=remove_money(money,464.0)
print(money)