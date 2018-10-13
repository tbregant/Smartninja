import random


def generate_loto_numbers(count):
    count = count
    number_list = []
    while True:
        random_num = random.randint(1,39)
        if random_num in number_list:
            continue
        number_list.append(random_num)
        if len(number_list) == count:
            break
    number_list.sort()
    return number_list


def main():
    print "Welcome to Lotto numbers generator"
    while True:
        numbers = int(raw_input("Please how many numbers would you like to generate: "))
        if numbers > 39:
            print "It's not possible to generate more than 39 numbers!"
            continue
        break
    print generate_loto_numbers(numbers)


if __name__ == '__main__':
    main()