# no external imports required

class JunctionBox():
    def __init__(self, x, y, z):
        self._x = int(x)
        self._y = int(y)
        self._z = int(z)
    
    def distance(self, other):
        dx = self._x - other._x
        dy = self._y - other._y
        dz = self._z - other._z
        return dx*dx + dy*dy + dz*dz

    # Connect jb to other_jb
    def __eq__(self, value):
        return (self._x == value._x and self._y == value._y and self._z == value._z)
    
    def __hash__(self):
        return hash((self._x, self._y, self._z))
    
    def __lt__(self, other):
        return (self._x, self._y, self._z) < (other._x, other._y, other._z)
    
    def __str__(self):
        return f"{self._x}, {self._y}, {self._z}"

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
        return self._circuit == value._circuit
    
    def __hash__(self):
        return hash(tuple(sorted(self._circuit)))
    
    def __str__(self):
        return str([str(x) for x in self._circuit])
        

# def add_jb_existing_ciruits(circuit, connected_circuits):
#     # Connect jb to other_jb
#     # is junctionbox already in a circuit
#      # Check if any jbs are present already in connected ciruit
#     for jb in circuit._circuit:
#         # if any of these are already in a connected circuit, add to that circuit
#         for conn_circuit in connected_circuits:
#             if jb in conn_circuit._circuit:
#                 # add all jbs in our circuit to that connected circuit
#                 for jb_add in circuit._circuit:
#                     conn_circuit.add_junciton_box(jb_add)
#                 # We want to connect that jb to that existing circuit
#                 return True
#     return False

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
total_jps = 0
with open(r"C:\Projects\Code\AOC\2025 - python\day-8\problem.txt") as target:
    

    for line in target:
        new_line = line.strip()
        x, y, z = line.split(",")
        unconnected_junction_boxes.append(JunctionBox(x,y,z))
        total_jps += 1

# for jb in unconnected_junction_boxes:
#     nearest_jb = None
#     nearest_jb_distance = None

#     for other_jb in unconnected_junction_boxes:
#         if jb == other_jb:
#             continue
#         if nearest_jb is None:
#             nearest_jb = other_jb
#             nearest_jb_distance = jb.distance(other_jb)
#         if jb.distance( other_jb) < nearest_jb_distance:
#             nearest_jb = other_jb
#             nearest_jb_distance = jb.distance(other_jb)

#     circuit_pairs.add(Circuit(jb, nearest_jb, nearest_jb_distance))

# sorted_list = sorted(circuit_pairs)

# build all pairwise circuits (each unordered pair exactly once)
for i in range(len(unconnected_junction_boxes)):
    for j in range(i+1, len(unconnected_junction_boxes)):
        a = unconnected_junction_boxes[i]
        b = unconnected_junction_boxes[j]
        dist = a.distance(b)
        circuit_pairs.add(Circuit(a, b, dist))

sorted_list = sorted(circuit_pairs)

# --- Part 1: process the 1000 shortest pairs and print product of sizes of top 3 circuits
connected_circuits = []
total_pairs = min(1000, len(sorted_list))
for idx in range(total_pairs):
    circuit = sorted_list[idx]
    if not add_jb_existing_ciruits(circuit, connected_circuits):
        connected_circuits.append(circuit)

sizes = sorted([len(c._circuit) for c in connected_circuits], reverse=True)
prod = 1
for s in sizes[:3]:
    prod *= s
print(prod)

# --- Part 2: iterate pairs until all boxes are in one circuit; print product of X coords of the final connecting pair
connected_circuits_full = []
for circuit in sorted_list:
    if not add_jb_existing_ciruits(circuit, connected_circuits_full):
        connected_circuits_full.append(circuit)
    if len(connected_circuits_full) == 1 and len(connected_circuits_full[0]._circuit) == len(unconnected_junction_boxes):
        pair = list(circuit._circuit)
        xprod = pair[0]._x * pair[1]._x
        print(xprod)
        break