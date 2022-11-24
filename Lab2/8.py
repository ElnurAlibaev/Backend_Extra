money=4640.0
currency="KZT"

def add_money(x:float)->None:
    global money
    money+=x

def remove_money(x:float)->None:
    global money
    money-=x

def recount_money()->None:
    global money,currency
    if currency=="KZT":
        currency="USD"
        money=money/464
    else:
        currency="KZT"
        money=money*464

add_money(464)
print(money, currency)

remove_money(464)
print(money, currency)

recount_money()
print(money, currency)

recount_money()
print(money, currency)