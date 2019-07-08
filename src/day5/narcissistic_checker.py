'''
Input: Integer from keyboard
Output: True or False, that the input integer is a narcissistic number
Method: narcissistic number is a number obtained by summing up cube of its every digits,
'''


def power_of_list(input_list, power_val):
    # power elements in input_list by power_val
    return [pow(x, power_val) for x in input_list]


def narcis_checker(input_number):
    str_num_list = list(str(input_number))
    input_num_list = list(map(int, str_num_list))
    input_num_list = power_of_list(input_num_list, 3)
    if sum(input_num_list) == input_number:
        print('The number %d is naricissistic' % input_number)
    else:
        print('The number %d is NOT naricissistic' % input_number)


if __name__ == '__main__':
    narcis_checker(153)
