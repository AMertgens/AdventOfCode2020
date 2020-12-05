def read_file():
    with open('02input.txt') as f:
        return [line.strip().split(":") for line in f.readlines()]

def solve(pwdlist):
    part1_counter = 0
    part2_counter = 0
    for line in pwdlist:
        letter= line[0].split()[1]
        min_max = line[0].split()[0].split("-")
        pwd = line[1]
        if  int(min_max[0]) <= pwd.count(letter) <= int(min_max[1]):
            part1_counter += 1
        if (bool(pwd[int(min_max[0])] == letter) ^ bool(pwd[int(min_max[1])] == letter)) :
            part2_counter += 1                  
    return(part1_counter,part2_counter)

input = read_file()
print (solve(input))


