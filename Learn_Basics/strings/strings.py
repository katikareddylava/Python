street ="Aero Nagar"
city="Hyderabad"
country="India"
address = street+"\n"+city+"\n"+country
print("Full address: ",address)
address = f'{street}\n{city}\n{country}'
print("Address using f-string:",address+"\n")

statement = "Earth revolves around the sun"
print(statement[6:14])
print(statement[-3]+"\n")

fruits =3
veg = 6
print(f'I eat {veg} veggies and {fruits} fruits daily \n')

s='maine 200 banana khaye'
s = s.replace('banana','samosa').replace('200','10')
print(s)