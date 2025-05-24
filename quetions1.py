def buildTree(word: str) -> str:
    if not word:
        return ""

    # 1-D array large enough for a worst-case degenerate tree
    tree = [None] * (2 ** len(word))
    pos = {}
    
    def insert(ch: str, i: int = 0) -> None:
        """Recursive BST insert that records the final index."""
        if tree[i] is None:
            tree[i] = ch
            pos[ch] = i
        elif ch < tree[i]:
            insert(ch, 2 * i + 1) # left
        else:
            insert(ch, 2 * i + 2) # right

    # build the whole tree
    for ch in word:
        insert(ch)

    # indices in ascending order, then gaps between neighbours
    indices = sorted(pos.values())
    gaps = [indices[i] - indices[i - 1] - 1 for i in range(1, len(indices))]

    return " ".join(map(str, gaps))

print(buildTree('GASTON'))