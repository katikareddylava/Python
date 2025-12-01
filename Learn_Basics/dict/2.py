import statistics


stock_prices = {'info':[600, 630, 620],'ril':[1430,1490,1567],'mtl':[234,180,160]}


def print_all():
    for k,v in stock_prices.items():
        avg = statistics.mean(v)
        print(f'{k}==> {v}==> avg: {round(avg,2)}')

def add():
    stock = input("Enter stock name: ").lower()
    price = float(input("Enter the price: "))

    if stock not in stock_prices:
        stock_prices[stock]= [price]
        print_all()
        return
    else:
        stock_prices[stock].append(price)
        print_all()

user_input = input("Enter input type: ").lower()

if(user_input == 'print'):
    print_all()
elif(user_input == 'add'):
    add()