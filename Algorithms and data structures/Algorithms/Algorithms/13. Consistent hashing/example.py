# Rehashing happens automatically during adding the new server

def make_hash(key):
    hash_val = 0
    p = 53
    m = 360  # ring size
    for i, char in enumerate(key):
        hash_val = (hash_val + (ord(char) - ord('a') + 1) * (p ** i)) % m
    return hash_val


class ConsistentHashRing:
    def __init__(self, servers=None, virtual_servers_count=3):
        self.virtual_servers_count = virtual_servers_count
        self.ring = {}  # key: position, value: real server
        self.positions = []  # sorted list of positions on the ring
        # initial servers set up
        for server in servers:
            self.add_server(server)

    def add_server(self, server):
        for i in range(self.virtual_servers_count):
            # rehashing
            key = f"{server}_{i}"
            position = make_hash(key)
            self.ring[position] = server
            self.positions.append(position)
        self.positions.sort()

    def get_server(self, key):
        position = make_hash(key)
        for p in self.positions:
            if position <= p:
                return self.ring[p]
        return self.ring[self.positions[0]]  # wrap around the ring

    def remove_server(self, server):
        positions_to_remove = []
        for i in range(self.virtual_servers_count):
            key = f"{server}_{i}"
            position = make_hash(key)
            if position in self.ring:
                del self.ring[position]
                positions_to_remove.append(position)
        # Remove positions from the list and re-sort
        self.positions = [p for p in self.positions if p not in positions_to_remove]
        self.positions.sort()


# Step 1: Create ring with 3 servers
ring = ConsistentHashRing(servers=["A", "B", "C"], virtual_servers_count=3)

# Step 2: Track key -> server assignments before adding a new server
keys = ["User123", "User456", "User789", "UserABC", "UserXYZ"]
assignments_before = {key: ring.get_server(key) for key in keys}

print("\nAssignments before adding D:")
for key, server in assignments_before.items():
    print(f"{key} -> {server}")

# Step 3: Add new server D
ring.add_server("D")

# Step 4: Track key -> server assignments after adding the new server
assignments_after = {key: ring.get_server(key) for key in keys}

print("\nAssignments after adding D:")
for key, server in assignments_after.items():
    print(f"{key} -> {server}")

# Step 5: Show which keys changed servers (rehashing effect)
print("\nKeys that were reassigned to a different server:")
for key in keys:
    if assignments_before[key] != assignments_after[key]:
        print(f"{key}: {assignments_before[key]} -> {assignments_after[key]}")

ring.get_server("UserABC")
