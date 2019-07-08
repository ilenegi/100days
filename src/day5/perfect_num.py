'''
Input: Integer
Output: whether the input integer is a perfect number
Method: find the greatest common divisor (gcd), add the divisor from 1 to gcd
'''
import math

def perfect_checker(input_number):
    tmp_sum = [1]
    for divisor_elem in range(2, int(math.sqrt(input_number))+1):
        if input_number % divisor_elem == 0:
            tmp_sum = tmp_sum + [divisor_elem, int(input_number/divisor_elem)]
    if sum(tmp_sum) == input_number:
        print('The number %d is perfect. The divisors are: ' % input_number, tmp_sum)
    else:
        print('The number %d is NOT perfect. The divisors are: ' % input_number, tmp_sum)


if __name__ == '__main__':
    perfect_checker(150)
