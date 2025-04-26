n = 73
k = 15
essay = '''
I bought a property in Egypt and what they do for you is give you the property, you then get to go and customize it however you want, which only costed me £4,000 for the kitchen, for the outdoor furniture, for the TV, for the AC, for the bedroom furniture, for the sofa bed. After that, the management of the building will manage your property for you while you put it on AirBNB.
'''
def formater(n, k, essay):
    words = essay.split()
    lines = []
    curcount = 0
    curline = []
    for word in words:
        if curcount + len(word) > k:
            lines.append(' '.join(curline))
            curcount = len(word)
            curline = [word]
        else:
            curcount += len(word)
            curline.append(word)
    if curline:
        lines.append(' '.join(curline))

    return lines

x = formater(n,k,essay)
for z in x:
    print(z + '\n')