import random
import time
import math



def guess_one():
    the_one = 100
    one = random.randint(1 ,the_one)
    print(one)
    bingo = True
    i = 1

    the_small_one = 1
    the_big_one = the_one

    guess_one = int(the_one/2)

    while bingo:
        if guess_one < one:
            print('第--{}--次猜数字是<{}>,小了'.format(i, guess_one), )
            # the_big_one = the_one
            the_small_one = guess_one
            print('[{}-{}]'.format(the_small_one, the_big_one))

            guess_one = int(guess_one + (the_big_one - guess_one)/2 + 1)
            print('猜错了，重新猜{}'.format(guess_one))
            
        elif guess_one > one:
            print('第--{}--次猜数字是<{}>，大了'.format(i, guess_one))
            the_big_one = guess_one
            print('[{}-{}]'.format(the_small_one, the_big_one), )
            guess_one = int( (the_small_one + guess_one)/2)
            print('猜错了，重新猜{}'.format(guess_one))
        elif guess_one == one + 1:
            pass

        elif guess_one == one:
            print('猜对了，{}={}'.format(guess_one, one))
            bingo = False
        i += 1
    print('总共猜了<<<{}>>>次'.format(i))
        # time.sleep(1)
    return i
    
    





x = 0
y = []
z = 0
while x < 100:
    y.append(guess_one())
    x += 1
print(y)
for i in y:
    z += i
print(z/100)
