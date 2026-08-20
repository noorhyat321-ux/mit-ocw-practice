def get_permutations(sequence):
    if len(sequence) <= 1:
        return [sequence]
    
    permutations = []
    first_char = sequence[0]
    rest = sequence[1:]
    
    for p in get_permutations(rest):
        for i in range(len(p) + 1):
            permutations.append(p[:i] + first_char + p[i:])
    return list(set(permutations))
