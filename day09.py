with open("input09.txt") as i:
    input = i.read().strip()

test_data = """2333133121414131402"""

# input = test_data

total_size = 0
files = []
free_blocks = []
for i, b in enumerate([int(x) for x in input]):
    if i%2 == 0:
        files.append((i//2, b, total_size))
    else:
        free_blocks.append((b, total_size))
    total_size += b


blocks = [None] * total_size
for file in files:
    id, size, start = file
    for i in range(start, start+size):
        blocks[i] = id

start = 0
end = len(blocks)-1
while start<end:
    while blocks[start] is not None:
        start += 1
    while blocks[end] is None: end -= 1
    if start<end:
        blocks[start] = blocks[end]
        blocks[end] = None

checksum = sum([i*x for i,x in enumerate(blocks) if x is not None])
print(checksum)

blocks = [None] * total_size
for j in range(len(files)-1, 0, -1):
    id, size, start = files[j]
    for i in range(0, j):
        block_size, block_start = free_blocks[i]
        if block_size>=size:
            files[j] = id, size, block_start
            free_blocks[i] = block_size-size, block_start+size
            break

checksum = 0
for id, size, start in files:
    for i in range(size):
        checksum += id*(start+i)

print(checksum)
