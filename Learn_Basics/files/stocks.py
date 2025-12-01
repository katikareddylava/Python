import csv
with open("D:\\AI\\Python\\Learn_Basics\\files\\stocks.csv" ,"r") as f, open("D:\\AI\\Python\\Learn_Basics\\files\\output.csv","w") as w:
    w.write("Company Name,PE Ratio, PB Ratio\n")
    reader = csv.reader(f)
    next(reader)     
    for tokens in reader:
        stock = tokens[0]
        price = float(tokens[1])
        eps = float(tokens[2])
        book = float(tokens[3])
        pe = round(price / eps, 2)
        pb = round(price / book, 2)
        w.write(f"{stock},{pe},{pb}\n")