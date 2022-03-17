import random;

numHeads = 0
numTails = 0

for i in range(100):  
    coin = random.randrange(0,2)

    if coin == 0:
        numHeads += 1
    elif coin == 1:
        numTails += 1

print("Number of Heads:", numHeads)
print("Number of Tails:", numTails)