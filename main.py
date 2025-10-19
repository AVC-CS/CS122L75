
def getInput():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    numbers = list(map(int, input().split()))
    return numbers

def findMost(numbers):
    """
    ########################################
    Code Your Program here
    ########################################
    """
    maxf = numbers.count(numbers[0]); most = numbers[0]
    for i in range(len(numbers)):
        freq = numbers.count(numbers[i])
        if freq > maxf:
            maxf = freq
            most = numbers[i] 
    return most


def main():
    numbers = getInput()
    ret = findMost(numbers)
    print(f'The most frequently used numbers is: {ret}')


if __name__ == '__main__':
    main()
