import time

def read_file():
    with open('06input.txt') as f:
        bp_list2 = [group for group in f.read().strip().split("\n\n")]
    return( bp_list2)

def solve(Input):
    sum1= 0
    sum2= 0
    for group in Input:
        sum1+= len(list(set(group.replace("\n", ""))))
        groupsplit = group.split("\n")
        if len(groupsplit) > 1:
            setlist = [set(x) for x in groupsplit]
            sum2 += len(setlist[0].intersection(*setlist))         
        else:
            sum2 += len(groupsplit[0])
    return(sum1,sum2)

Input = read_file()
start = time.perf_counter()
print(solve(Input), " in ", time.perf_counter() - start, " seconds.")