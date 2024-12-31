def parse_input():
    f = open("2024\Day 5\\input_1.txt", "r")
    rules = list()
    updates = list()
    for line in f:
        line = line.strip()
        if "|" in line:
            rules.append(line.split("|"))
        elif len(line) == 0:
            continue
        else:
            updates.append(line.split(","))
    return rules, updates

def is_valid_update(update):
    for page in range(0,len(update)):
        # Are all other pages after this page not before in the rules
        cur_page = update[int(page)]
        other_pages = list()
        if page + 1 < len(update):
            other_pages = update[page+1: ]
        for othr_page in other_pages:
            for rule in rules:
                if othr_page in rule and cur_page in rule:
                    if othr_page == rule[0] and cur_page == rule[1]:
                        return False
    return True

def is_valid_correct(update):
    for page in range(0,len(update)):
        # Are all other pages after this page not before in the rules
        cur_page = update[int(page)]
        other_pages = list()
        if page + 1 < len(update):
            other_pages = update[page+1: ]
        for othr_page in other_pages:
            for rule in rules:
                if othr_page in rule and cur_page in rule:
                    if othr_page == rule[0] and cur_page == rule[1]:
                        # Switch the values round
                        temp_index = update.index(othr_page)
                        update[page] = othr_page
                        update[temp_index] = cur_page
                        return False
    return True

def get_median_value(update):
    return int(update[int(len(update)//2)])
    
rules, updates = parse_input()
valid_updates = 0
total_middle_page = 0
for update in updates:
    if not is_valid_update(update):
        while not is_valid_correct(update):
            is_valid_correct(update)
        total_middle_page += get_median_value(update)
    print(is_valid_update(update))
print(f"{total_middle_page}")