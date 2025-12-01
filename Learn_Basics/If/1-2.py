india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city1 = input("Enter city one: ")
city2 = input("Enter city two: ")


if(city1 in india and city2 in india):
    print(f"Both cities are in india")
elif(city1 in pakistan and city2 in pakistan):
    print(f"Both cities are in pakistan")
elif(city1 in bangladesh and city2 in bangladesh):
    print(f"Both cities are in bangladesh")
else:
    print("They don't belong to same country")