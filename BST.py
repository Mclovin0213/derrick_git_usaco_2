def buildTree(word: str) -> str:
    if not word:
        return ""

    # Array allocated with big enough size for word
    tree = [None] * (2 ** len(word))
    
    # Dictionary stores the positions of each letter in the array
    pos = {}
    
    # Helper function to insert a node in an array
    def insert(ch: str, i: int = 0) -> None:
        """Recursive BST insert that records the final index."""
        if tree[i] is None:
            tree[i] = ch
            pos[ch] = i
        elif ch < tree[i]:
            insert(ch, 2 * i + 1) # left
        else:
            insert(ch, 2 * i + 2) # right

    # Build the whole tree, by inserting each letter of the word
    for ch in word:
        insert(ch)

    # Sort filled spots in the array
    indices = sorted(pos.values())
    
    
    gaps = [indices[i] - indices[i - 1] - 1 for i in range(1, len(indices))]

    return " ".join(map(str, gaps))

print(buildTree('GASTON'))