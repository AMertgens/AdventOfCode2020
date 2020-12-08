import time
searched_bag=  "shiny gold"
def read_file():
    with open('07input.txt') as f:
        baglist = [group.strip().replace("contain", "").replace("bags", "bag").split("bag") for group in f.readlines()]
    bagdict = {}
    for bag in baglist:
        
        bagdict[bag[0].strip()] = [ (s.replace(",","").strip()[0] ,s.replace(",","").strip()[1:].strip()) for s in bag[1:-1]]


    return(bagdict)

def solve(Input, searched):
    #print(Input)
    searchedbags = [searched ,]
    validbags = []        
    def check_bag(bag, contents):
        #print("check", bag)
        if contents[0][0] != "n":
            if bag not in validbags:
                flag = False
                for sub_bag in contents:
                    #print(sub_bag)
                    if sub_bag[1] in searchedbags or sub_bag[1] in validbags:
                        #print("true")
                        validbags.append(bag)
                        flag = True
                    else:
                        #print("false..searching...")
                        if sub_bag[1] in Input.keys():
                            validbag = check_bag(sub_bag[1], Input[sub_bag[1]])
                            if validbag:
                                validbags.append(bag)
                                flag = True
                return flag
            else:
                return True
        else:
            return False
    total = 1
    def count_bags(key, total):
        print("count_bags for: ", key)     
        for bag in Input[key]:
            n, col = bag
            print(n, col)
            if n != "n":
                total = total + (n * count_bags(col))
            print(total)
            


    for key, value in Input.items():
        #print("search",searchedbags)    
        #print("valid",validbags)
        #time.sleep(0.5)
        if value[0][1] in Input.keys():
            is_valid = check_bag(key,value)
            #print(key, is_valid)
            if is_valid:
                validbags.append(key)
        if key == searched:
            count = count_bags(key, total)
    return(len(set(validbags)))
        
  

Input = read_file()
start = time.perf_counter()
print(solve(Input, searched_bag ), " in ", time.perf_counter() - start, " seconds.")