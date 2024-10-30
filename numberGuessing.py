# NUMBER GUESSING GAME
import time

targetNum = input("Enter the target number: ")
intNum = int(targetNum)

len = len(targetNum)
currentNum = 10000000000000000
st = time.time()

while currentNum != intNum:
    print(currentNum)
    currentNum+=1

ft = time.time()
numPerSec = round(currentNum/(ft-st),0)

print('The number is: ', currentNum)
print('Decrypted in: ', ft-st)
print('Number per second: ', numPerSec)

