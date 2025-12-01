word_stats ={}

with open("D:\\AI\\Python\\Learn_Basics\\files\\poem.txt","r") as f:
    for line in f:
        words = line.split()
        for word in words:
            if word in word_stats:
                word_stats[word] += 1
            else:
                word_stats[word] = 1
    
word_occurences = word_stats.values()
max_count = max(word_occurences)
print("Max occurances of any word is:",max_count)

for k,v in word_stats.items():
    if(v == max_count):
        print(f'Max count word {k}. No of times occured: {v}')
        break
