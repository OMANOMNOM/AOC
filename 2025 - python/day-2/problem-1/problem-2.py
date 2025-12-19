
def check_is_valid_id_problem_2(id):
    """return ID if invalid or None.

    ID is invalid if if id is made up of some sequence of digis repeated at least twice
    """
    # Loop through possible sequence lengths
      # Loop through all possible sequences of that length
        # Get that sequence
        # Check if repeating that sequence forms the entire ID
        # If invalid ID return ID
    # else Return None

    # Loop through possible sequence lengths
    for seq_length in range(1, len(id)//2 + 1):  # NOTE not sure this is correct
      # Loop through all possible sequences of that length
      for start_index in range(0, len(id) - seq_length + 1): 
        sequence = id[start_index:start_index + seq_length]
        repeated_sequence = sequence * (len(id) // seq_length)
        # Check if repeating that sequence forms the entire ID
        if repeated_sequence == id:
            return id
    return None



def check_is_valid_id_problem_1(id):
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

            invalid_id = check_is_valid_id_problem_2(id_str)
            if invalid_id is None:
                pass
            else:
                print(f"invalid ID found: {invalid_id}")
                total_count += int(invalid_id)

print(f"total count of invalid IDs: {total_count}")
            
                