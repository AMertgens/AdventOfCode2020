def read_file():
    with open('01input.txt') as f:
        return [int(line) for line in f.readlines()]

def solve(numlist):
    for i in numlist:   
        for j in numlist:
            for k in numlist:
                if (i + j + k) == 2020:
                        return (i*j*k)

numlist = read_file()
print(solve(numlist))
