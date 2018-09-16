import random
import time
import math

bingo = True
the_one = 10000
one = random.randint(1 ,the_one)
print(one)
i = 1

def guess_one():
    guess_one = int(the_one/2)

    while bingo:
        if guess_one < one:
            print('第{}次猜数字是<{}>,小了'.format(i, guess_one))
            guess_one = int(guess_one + math.sqrt(one - guess_one) + 1)
            print('猜错了，重新猜{},正确是{}'.format(guess_one, one))
        elif guess_one > one:
            print('第{}次猜数字是<{}>，大了'.format(i, guess_one))
            guess_one = int(1 +  math.sqrt(guess_one - one))
            print('猜错了，重新猜{},正确是{}'.format(guess_one, one))
        elif guess_one == one + 1:
            pass

        elif guess_one == one:
            print('猜对了，{}={}'.format(guess_one, one))
            bingo = False
        i += 1
        time.sleep(1)
    
    



def guess_two():
    guess_one = int(the_one/2)
    i = 1
    while True:
        if guess_one < one:
            print('第{}次猜数字是<{}>,小了'.format(i, guess_one))
            guess_one = int(guess_one + math.sqrt(one - guess_one))
            print('猜错了，重新猜{},正确是{}'.format(guess_one, one))
        elif guess_one > one:
            print('第{}次猜数字是<{}>，大了'.format(i, guess_one))
            guess_one = int(math.sqrt(guess_one))
            print('猜错了，重新猜{},正确是{}'.format(guess_one, one))
        elif guess_one == one + 1:
            pass

        elif guess_one == one:
            print('猜对了，{}={}'.format(guess_one, one))
            bingo = False
        i += 1
        time.sleep(1)
        if i > 15:
            break




guess_one()
