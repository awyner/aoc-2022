def main():
    nums = []
    result = []
    with open("day25\\input.txt") as f:
        for line in f:
            nums.append(line.strip())
        for num in nums:
            result.append(snafuToDec(num))
            # result.append(decToSnafu(num))
        sum = 0
        for x in result:
            sum += x
        print(decToSnafu(sum))
   

def snafuToDec(snafu):
    place = len(snafu) - 1
    dec = 0
    for char in snafu:
        if char == '=':
            char = -2
        elif char == '-':
            char = -1
        else:
            char = int(char)
        char *= (5 ** place)
        dec += char
        place -= 1
    # print(dec)
    return dec


def decToSnafu(dec):
    snafu = ''
    while dec > 0:
        remain = dec % 5
        if remain == 0:
            snafu += '0'
        elif remain == 1:
            snafu += '1'
        elif remain == 2:
            snafu += '2'
        elif remain == 3:
            snafu += '='
            dec += 2
        elif remain == 4:
            snafu += '-'
            dec += 1
        dec //= 5
    snafu = snafu[::-1]
            
    return snafu


main()
