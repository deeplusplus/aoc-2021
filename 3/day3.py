
def main():
    file = open('day3input.txt', 'r')
    lines = file.readlines()

    digit_sum_list = []
    num_lines = len(lines)
    threshold = num_lines / 2
    epsilon_binary_string = ""
    gamma_binary_string = ""

    for index in range(0, 12):
        sum = 0
        for line in lines:
            sum += int(line[index])
        digit_sum_list.append(sum)

    print(digit_sum_list)


    # epsilon
    for digit in digit_sum_list:
        if digit >= threshold:
            epsilon_binary_string += "1"
        else:
            epsilon_binary_string += "0"

    # epsilon
    for digit in digit_sum_list:
        if digit >= threshold:
            gamma_binary_string += "0"
        else:
            gamma_binary_string += "1"

    epsilon_int = int(epsilon_binary_string, 2)
    gamma_int = int(gamma_binary_string, 2)

    print("Espilon binary:", epsilon_binary_string)
    print("Gamma binary:", gamma_binary_string, "\n")
    print("Epsilon int:", epsilon_int)
    print("Gamma int:", gamma_int)

    print("Power Consumption: ", gamma_int * epsilon_int)

if __name__ == "__main__":
    main()