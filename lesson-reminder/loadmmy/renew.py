n = eval(input('Please input how many lessones you have in a day'))
for i in range(7):
    for j in range(0,n):
        fp = open(f"{i}-{j}.json",'w')