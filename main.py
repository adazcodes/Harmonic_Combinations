import itertools

def print_filtered_permutations(arr, constraints):
    perms = itertools.permutations(arr)
    count = 1  # Sequential index for valid permutations
    for p in perms:
        if all(p[idx] in vals for idx, vals in constraints.items()):
            formatted = ', '.join(str(x) for x in p)
            print(f'{count}: ({formatted})')
            count += 1

# Edit HERE for jazz pattern
array = [1,3,5,8]  # Mixed int and str elements

# Downbeats must be harmony notes, including extended tones
# Edit HERE for downbeat constraints
constraints = {
    0: [1, 5, 8],
    2: [1, 5, 8]
}

print_filtered_permutations(array, constraints)
