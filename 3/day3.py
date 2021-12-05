###
###
###
######## THE PROCESS OF DISCRIMINATING NUMBERS IN AND OUT NEED TO BE APPLIED TO THE RESULTS THAT DISCRIMINATION PRODUCES.  BIT BY BIT.
###
###
###

def main():
    file = open('day3input.txt', 'r')
    lines = file.readlines()

    digit_sum_list = []
    num_lines = len(lines)
    threshold = 500
    most_common_string = ""
    least_common_string = ""

    for index in range(0,12):
        sum = 0
        for line in lines:
            sum += int(line[index])
        digit_sum_list.append(sum)

    print(digit_sum_list)


    # most common bits
    for digit in digit_sum_list:
        if digit >= threshold:
            most_common_string += "1"
        else:
            most_common_string += "0"

    # least common bits
    for digit in digit_sum_list:
        if digit >= threshold:
            least_common_string += "0"
        else:
            least_common_string += "1"

    print("Least Common: ", least_common_string)    
    print("Most Common: ", most_common_string)
    print(int(least_common_string, 2) * int(most_common_string,2))

if __name__ == "__main__":
    main()