result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

head_count = 0
for val in result:
    if(val == 'heads'):
        head_count += 1

print("Head count: ",head_count)


for i in range(1,11):
    if(not i%2 == 0):
        print(f'Square number: {i*i}')

month_list = ["January", "February", "March", "April", "May"]
expense_list = [2340, 2500, 2100, 3100, 2980]

e = int(input('Enter expense amount: '))
month = -1
for i in range(len(expense_list)):
    if(e == expense_list[i]):
        month = i
        break

if month != -1:
    print(f'You spent {e} in {month_list[month]}')
else:
    print(f'You didn\'t spend {e} in any month')


race = 5

for i in range(race):
    km = i+1
    if(km != race):
        tired = input(f"you ran {km} KM.are you tired: ")
        if(tired == 'yes'):
            print(f"you ran {km} KM.you didn't finish the race")
            break
    else:
        print("congratulations you finised the race")

for r in range(1,6):
    s = ''
    for c in range(r):
        s += '*'
    print(s+"\n")

        



