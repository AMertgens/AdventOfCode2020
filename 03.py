slopes = [
    [1,1],
    [3,1],
    [5,1],
    [7,1],
    [1,2],
]

def read_file():
    with open('03input.txt') as f:
        return [lines.strip() for lines in f.readlines()]

def treecounter(map, right, down):
    h_index = 0
    treecount = 0
    for i in range(0, len(map), down):
        line = map[i]
        if line[h_index % len(line)] == "#":
            treecount += 1
        h_index += right
    return treecount

def totaltrees(slopes):
    totaltreeprod = 1
    for slope in slopes:
        totaltreeprod *= treecounter(map, slope[0], slope[1])
    return(totaltreeprod)

map = read_file()
print(treecounter(map, 3, 1), totaltrees(slopes)) 