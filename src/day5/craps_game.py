'''
Input: no
Output: player won or the machine won
Method: each round throw the dice twice, in the first round, if the sum of two draws is 7
or 11, player won. If the sum is 2, 3 or 12 machine won. Otherwise, keep this sum, if this
sum number appears again, the player won. Before that, if the sum number 7 appear, the machine won.
'''

import random


def one_draw():
    return random.randint(1, 6)


def craps_game():
    tmp_iteration = 1
    tmp_mem = 0
    while True:
        rand_sum = one_draw() + one_draw()
        if tmp_iteration == 1:
            if rand_sum in [7, 11]:
                print('Player won after %d iteration. The sum is %d.' % (tmp_iteration, rand_sum))
                break
            elif rand_sum in [2, 3, 12]:
                print('The machine won after %d iteration. The sum is %d.' % (tmp_iteration, rand_sum))
                break
            else:
                tmp_mem = rand_sum
                tmp_iteration += 1
        else:
            if rand_sum == 7:
                print('The machine won after %d iteration. The sum is %d.' % (tmp_iteration, rand_sum))
                break
            elif rand_sum == tmp_mem:
                print('Player won after %d iteration. The sum is %d.' % (tmp_iteration, rand_sum))
                break
            tmp_iteration += 1


if __name__ == '__main__':
    for _ in range(20):
        craps_game()


