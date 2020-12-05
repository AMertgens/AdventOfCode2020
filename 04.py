req_field = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
opt_field = ["cid"]
byr_val = [1920, 2002]
iyr_val = [2010, 2020]
eyr_val = [2020, 2030]
hgt_val = [[150,193], [59,76]]
ecl_val = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
hcl_chars = "0123456789abcdef"
pid_length = 9

#bonus condition: no REGEX!

def read_file():
    with open('04input.txt') as f:
        return f.read().split("\n\n")

def validate_date(date, val):
    if len(date) == 4 and int(date) >= val[0] and int(date) <= val[1]:    
        return True

def validate_hgt(hgt,hgt_val):
    if hgt[-2:] == "cm":
        if int(hgt[:-2]) >= hgt_val[0][0] and int(hgt[:-2]) <= hgt_val[0][1]:
            return True
    elif hgt[-2:] == "in":
        if int(hgt[:-2]) >= hgt_val[1][0] and int(hgt[:-2]) <= hgt_val[1][1]:
            return True

def validate_hcl(hcl, chars):
    if hcl[0] == "#" and len(hcl) == 7:
        for c in hcl[1:]:
            if c not in chars:
                return False
        return True

def validate_ecl(ecl, vals):
    if ecl in vals:
        return True

def validate_pid(pid, length):
    if len(pid) == length:
        return(True)

def validate_pass(pas):    
    pas_dict = {}
    for field in pas:
        if field.split(":")[0] != "cid":
            pas_dict[field.split(":")[0]] = field.split(":")[1]
    if (
        validate_date(pas_dict["byr"], byr_val) and
        validate_date(pas_dict["iyr"], iyr_val) and
        validate_date(pas_dict["eyr"], eyr_val) and
        validate_hgt(pas_dict["hgt"], hgt_val)  and
        validate_hcl(pas_dict["hcl"], hcl_chars) and
        validate_ecl(pas_dict["ecl"], ecl_val) and
        validate_pid(pas_dict["pid"], pid_length)
    ):       
        return True
def solve(pass_list):
    part1valid = 0
    part2valid = 0 
    for p in pass_list:
        fields = []
        for field in p.split():
            fields.append(field.split(":")[0])
        list_dif = [i for i in req_field + fields if i not in req_field or i not in fields]
        if  list_dif == [] or  list_dif == opt_field:
            part1valid += 1
            if validate_pass(p.split()):
                part2valid += 1
    return (part1valid,part2valid)

pass_list = read_file()
print(solve(pass_list))


