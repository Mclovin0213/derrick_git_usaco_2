n = 5
m = [4,6,7,6]

def lineup(n, m):
    emeralds = set(range(1, n+1))
    result = None
    
    for first in emeralds:
        for second in emeralds:
            if first + second != m[0]:
                continue
            if first == second:
                continue
            x = [first, second]
            y = {first, second}

            valid = True

            for i in range(1, n - 1):
                next = m[i] - x[-1]
                if next not in x or next in y:
                    valid = False
                    break
                x.append(next)
                y.add(next)
            if valid:
                if result is None or x < result:
                    result = x
    return result
val = lineup(n,m)

print(' '.join(map(str, val)))