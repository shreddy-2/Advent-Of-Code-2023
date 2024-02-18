#Example 
'''
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

29, 83, 13, 24, 42, 14, 76
=>281
'''

keys = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def example():
    example_input = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]

    numbers = []

    for ex in example_input:
        out = []
        for c, char in enumerate(ex):
            for k, key in enumerate(keys):
                l = len(key)

                if ex[c: c+l] == key:
                    out.append(values[k])
        numbers.append(int(str(out[0]) + str(out[-1])))

    print(numbers)
    print(sum(numbers))


def actual():
    # Code to run on actual challenge

    input_full = []
    with open("input.txt", "r") as f:
        input_full = f.readlines()

    numbers = []

    for ex in input_full:
        out = []
        for c, char in enumerate(ex):
            for k, key in enumerate(keys):
                l = len(key)

                if ex[c: c+l] == key:
                    out.append(values[k])
        numbers.append(int(str(out[0]) + str(out[-1])))

    print(numbers)
    print(sum(numbers))



#example()
actual()    
