india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

userInput = input("Enter the city name:")

if(userInput in india):
    print(f"City {userInput} belongs to india")
elif(userInput in pakistan):
    print(f"City {userInput} belongs to pakistan")
elif(userInput in bangladesh):
    print(f"City {userInput} belongs to bangladesh")
else:
    print("City does not belong to any country")
