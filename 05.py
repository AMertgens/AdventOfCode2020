import time
rows = 128
columns = 8

def read_file():
    with open('05input.txt') as f:
        bp_list = [line.strip() for line in f.readlines()]
    return(bp_list)

def solve(Input):
    solution = []
    myseat = 0

    # Part One
    for bp in Input:
        row= [0, rows]
        column = [0, columns]
        for char in bp:
            if char == "F":
                row[1] = row[1] - ((row[1]-row[0]) / 2)
            elif char == "B":
                row[0] = row[0] + ((row[1]-row[0]) / 2)
            elif char == "L":
                column[1] = column[1] - ((column[1]-column[0]) / 2)
            elif char == "R":
                column[0] = column[0] + ((column[1]-column[0]) / 2)
        solution.append(int(row[0]) * 8 + int(column[0]))

    #Part Two    
    for i in range(min(solution),max(solution)+1):       
        if i-1 in solution and i+1 in solution and i not in solution:
            myseat = i
    
    return [max(solution),myseat]

Input = read_file()
start = time.perf_counter()
print(solve(Input), " in ", time.perf_counter() - start, " seconds.")