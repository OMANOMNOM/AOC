
def check_is_valid_id(id):
    """return ID if invalid or None.
    """
    if len(id) % 2 != 0:
        return None
    if id[len(id)//2:] == id[0:len(id)//2]:
        return id
    return None

for line in open(r"C:\Projects\Code\AOC\2025 - python\day-2\problem-1\problem-1.txt"):
    ranges = line.strip().split(',')
    total_count = 0
    for r in ranges:
        start, end = r.split('-')
        for id in range(int(start), int(end)+1):
            id_str = str(id)

            invalid_id = check_is_valid_id(id_str)
            if invalid_id is None:
                pass
            else:
                print(f"invalid ID found: {invalid_id}")
                total_count += int(invalid_id)

print(f"total count of invalid IDs: {total_count}")
            
                