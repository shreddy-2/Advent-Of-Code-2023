# Example
'''
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
asdkjfbasfngasdf

12, 38, 15, 77
=> 142
'''

import numpy as np


def example():
    # Code testing on example input
    example_input = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet", "asdkjfbasfngasdf"]

    input_numbers = np.zeros((len(example_input), 1))
    for i, string in enumerate(example_input):
        numbers = np.array([int(c) for c in example_input[i] if c.isdigit()])
        if len(numbers) == 0:
            input_numbers[i] = 0
        else:
            input_numbers[i] = int(''.join([str(numbers[0]), str(numbers[-1])]))

    final_value = int(np.sum(input_numbers))

    print(input_numbers)
    print(final_value)



def actual():
    # Code to run on actual challenge
    #input_full = open("input.txt", "r").read()

    input_full = []
    with open("input.txt", "r") as f:
        input_full = f.readlines()

    print(input_full[0], type(input_full[0]))
    
    input_numbers = np.zeros((len(input_full), 1))
    for i, string in enumerate(input_full):
        numbers = np.array([int(c) for c in string if c.isdigit()])
        if len(numbers) == 0:
            input_numbers[i] = 0
        else:
            input_numbers[i] = int(''.join([str(numbers[0]), str(numbers[-1])]))

    print(input_numbers)
    final_value = int(np.sum(input_numbers))
    print("\nResult: ", final_value)


#example()
actual()