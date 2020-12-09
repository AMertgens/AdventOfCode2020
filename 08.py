import time
import copy

def read_file():
    with open('08input.txt') as f:
        file = [x.split() for x in f.readlines()]
    return file
    

def solve(Input):
    accum = 0
    pointer = 0
    visited_pointers = []
    active = True
    ended = False
    while active:
        #time.sleep(1)
        #print(pointer, visited_pointers)
        if pointer  in set(visited_pointers):
            return(ended ,accum)
        visited_pointers.append(pointer)
        if Input[pointer][0] == "nop":
            pointer += 1
        elif Input[pointer][0] == "acc":
            accum += int(Input[pointer][1])
            #print("acc", accum)
            pointer += 1
        elif Input[pointer][0] == "jmp":
            #print("jmp")
            pointer += int(Input[pointer][1])
        if pointer >= len(Input):
            ended = True
            return(ended, accum)

def meta_solve(Input):
    index = 0
    fixing = True
    Input = copy.deepcopy(Input)
    while fixing:
        
        test = copy.deepcopy(Input)
        instr = test[index][0]
        if instr == "nop":
            #print(test[index][0])
            test[index][0] = "jmp"
        elif instr == "jmp":
            #print(test[index][0])
            test[index][0] = "nop"

        #print(test)
        if solve(test)[0] == True:
            return(solve(test))
        index += 1
      
        if index >= len(test):
            fixing = False
    

Input = read_file()
start = time.perf_counter()
#print(solve(Input ), " in ", time.perf_counter() - start, " seconds.")
print(meta_solve(Input ), " in ", time.perf_counter() - start, " seconds.")