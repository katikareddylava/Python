sugar_level = float(input("Enter sugar level: "))

if(sugar_level > 100):
    print("Sugar level is high")
elif(sugar_level< 80):
    print("Sugar level is low")
else:
    print("Sugar level is noraml")