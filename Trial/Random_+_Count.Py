import random
count=0
random_num = random.randint(0, 5)
guessed_num = int(input('enter a number to guess'))
while count < 3:
    guessed_num = int(input('enter a number to guess'))
    if guessed_num > random_num:
        print("number too high", random_num)
    elif guessed_num < random_num:
        print('number too low', random_num)
    else:
        print('you guessed right', random_num)
        break
    print('you have tried')
    count +=1