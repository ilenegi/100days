'''
Input: number of money, number of chicken, price of each chicken
Output: number of different chicken
Method: enumerate two of three variables, and find if the solution of the third one is suitble
'''


def hundred_chicken(num_money, num_chicken, value_of_chicken):
    for first_elem in range(min(num_money // value_of_chicken[0], num_chicken)):

        for second_elem in range(min(num_money // value_of_chicken[1], num_chicken)):

            if (num_chicken - first_elem - second_elem) >= 0 and (
                    num_money - first_elem * value_of_chicken[0] - second_elem *
                    value_of_chicken[1] - (num_chicken - first_elem - second_elem) * value_of_chicken[2]) == 0:
                print('You can buy %d %d and %d chicken.' % (first_elem, second_elem,
                      (num_chicken - first_elem - second_elem)))


if __name__ == '__main__':
    hundred_chicken(100, 100, [5, 3, 1/3])
