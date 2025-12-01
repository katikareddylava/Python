country = {'china': 143,'india':136,'usa':32,'pakistan':21}
user_input = input("Enter type input: ").lower()

def print_all():
    for k,v in country.items():
        print(f'{k}==>{v}')

def add():
    user_country = input("Enter the country to add: ").lower()
    if(user_country in country):
        print("Country already exist in our dataset. Terminating")
        print(f'{user_country}==>{country[user_country]}')
        return
    else:
        user_pop =float(input(f'Enter population for {user_country}: '))
        country[user_country] = user_pop
        print_all()

def remove():
    remove_country = input("Enter the country to remove: ").lower()
    if(remove_country in country):
        del country[remove_country]
        print_all()
    else:
        print(f'{remove_country} not found!!') 

def query():
    query_country = input("Enter country name to query:").lower()
    if query_country not in country:
        print("Country doesn't exist in our dataset. Terminating")
        return
    print(f"Population of {query_country} is: {country[query_country]} crore")


if(user_input == 'print'):
    print_all()
elif(user_input == 'add'):
    add()
elif(user_input == 'remove'):
    remove()
elif(user_input == 'query'):
    query()

