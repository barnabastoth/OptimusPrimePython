def read_file(filename):
    with open(filename) as data:
        data_list = data.read().splitlines()
        return data_list


def find_primes(numbers, limit):
    primes = []
    for number in numbers:
        dividers = 0
        number = int(number)
        for divider in range(1, number+1, 2):
            remainder = number%divider
            if remainder == 0:
                dividers += 1

        if dividers == 2:
            primes.append(number)
        
        if len(primes) >= limit:
            break
    
    return primes
        
            

def main():
    datas = read_file("numbers.txt")
    print(find_primes(datas, 100))

if __name__ == '__main__':
    main()
