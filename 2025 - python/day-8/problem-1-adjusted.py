# use integer arithmetic for distance (squared) to avoid sqrt/pow

class JunctionBox():
    def __init__(self, x, y, z):
        self._x = int(x)
        self._y = int(y)
        self._z = int(z)
    
    def distance(self, other):
        # return squared Euclidean distance (no sqrt) for correct ordering
        dx = other._x - self._x
        dy = other._y - self._y
        dz = other._z - self._z
        return dx*dx + dy*dy + dz*dz

    # Connect jb to other_jb
    def __eq__(self, value):
        return (self._x == value._x and self._y == value._y and self._z == value._z)
    
    def __hash__(self):
        return hash((self._x, self._y, self._z))
    
    def __lt__(self, other):
        return (self._x, self._y, self._z) < (other._x, other._y, other._z)

class Circuit():
    def __init__(self, junction_box_a, junction_box_b = None, distance = None):
        self._circuit = {junction_box_a}
        if junction_box_b is not None:
            self.add_junciton_box(junction_box_b)
        self._distance = distance

    def add_junciton_box(self, new_junction_box):
        self._circuit.add(new_junction_box)

    def __lt__(self, other):
        return self._distance < other._distance
    
    # Connect jb to other_jb
    def __eq__(self, value):
        # Two circuits are equal when they contain the same set of junction boxes
        if not isinstance(value, Circuit):
            return False
        return self._circuit == value._circuit
    
    def __hash__(self):
        return hash(tuple(sorted(self._circuit)))

# def add_jb_existing_ciruits(circuit, connected_circuits):
#     # Connect jb to other_jb
#     # is junctionbox already in a circuit
#      # Check if any jbs are present already in connected ciruit
#     # Find all connected circuits that intersect with the new circuit
#     matching = []
#     for jb in circuit._circuit:
#         for conn_circuit in connected_circuits:
#             if jb in conn_circuit._circuit and conn_circuit not in matching:
#                 matching.append(conn_circuit)

#     if not matching:
#         return False

#     # Merge the new circuit into the first matching circuit
#     target = matching[0]
#     for jb_add in circuit._circuit:
#         target.add_junciton_box(jb_add)

#     # Merge any other matching circuits into target and remove them
#     for other in matching[1:]:
#         for jb2 in other._circuit:
#             target.add_junciton_box(jb2)
#         try:
#             connected_circuits.remove(other)
#         except ValueError:
#             pass

#     return True

def add_jb_existing_ciruits(circuit, connected_circuits):
    # Connect jb to other_jb
    # is junctionbox already in a circuit
     # Check if any jbs are present already in connected ciruit
    # Find all connected circuits that intersect with the new circuit
    matching = []
    for jb in circuit._circuit:
        for conn_circuit in connected_circuits:
            if jb in conn_circuit._circuit and conn_circuit not in matching:
                matching.append(conn_circuit)

    if not matching:
        return False

    # Merge the new circuit into the first matching circuit
    target = matching[0]
    for jb_add in circuit._circuit:
        target.add_junciton_box(jb_add)

    # Merge any other matching circuits into target and remove them
    for other in matching[1:]:
        for jb2 in other._circuit:
            target.add_junciton_box(jb2)
        try:
            connected_circuits.remove(other)
        except ValueError:
            pass

    return True

unconnected_junction_boxes = list()
circuit_pairs = set()

with open(r"C:\Projects\Code\AOC\2025 - python\day-8\test.txt") as target:
    for line in target:
        new_line = line.strip()
        if not new_line:
            continue
        x, y, z = new_line.split(",")
        unconnected_junction_boxes.append(JunctionBox(x, y, z))


# build all pairwise circuits (each unordered pair exactly once)
for i in range(len(unconnected_junction_boxes)):
    for j in range(i+1, len(unconnected_junction_boxes)):
        a = unconnected_junction_boxes[i]
        b = unconnected_junction_boxes[j]
        dist = a.distance(b)
        circuit_pairs.add(Circuit(a, b, dist))

sorted_list = sorted(circuit_pairs)



connected_circuits = list()
# Loop through the shortest circuit pairs and add to connected circuits
total_pairs = min(10, len(sorted_list))
for index in range(total_pairs):
    circuit = sorted_list[index]
    if not add_jb_existing_ciruits(circuit, connected_circuits):
        connected_circuits.append(circuit)

total_connections = 1
sorted_connected_circuits = sorted(connected_circuits, key = lambda u : len(u._circuit), reverse=True)
for i in range(0,3):
    total_connections *= len(sorted_connected_circuits[i]._circuit)
print(total_connections)