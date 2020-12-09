import time
from collections import deque 

def read_file():
    with open('09input.txt') as f:
        numlist = [int(line.strip()) for line in f.readlines()]
    return(numlist)


def solve(numlist):
    preamble = 25
    pointer= preamble 
    nums = deque(numlist[:preamble])
    running = True
    weak = 0
    while running:
        #print(numlist[pointer])
        #print(nums)
        valid = False
        target = 0
        for n in nums:
            for n2 in nums:
                if n != n2:
                    #time.sleep(0.5)
                    #print(n, n2, n + n2)
                    if n+n2 == numlist[pointer]:
                        valid = True
                        #print("valid")
        if valid:
            nums.popleft()
            nums.append(numlist[pointer])
            pointer += 1
            continue
        else:
            target = numlist[pointer]
            pointer = 0
            running = False
    # Part 2
    while True:
        sum = numlist[pointer]
        subpointer = 1
        searching = True
        nlist = [numlist[pointer],]
        while searching:
            nlist.append(numlist[pointer + subpointer])
            sum += numlist[pointer + subpointer]
            if sum > target or pointer+subpointer >= len(numlist):
                searching = False
            if sum == target:
                weak = max(nlist) + min(nlist)
                searching = False
            subpointer += 1
        if weak == 0:
            pointer += 1
            continue
        else:
            searching = False


                
            

        return (numlist[pointer], weak)

    #print(nums)
   

Input = read_file()
start = time.perf_counter()
print(solve(Input), " in ", time.perf_counter() - start, " seconds.")