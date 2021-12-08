with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    a=[{"digits": l.split(" ")[:10], "out": l.split(" ")[11:]} for l in lines]

valid = [set(x) for x in ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]]

def is_valid(translation, digits):
    global valid
    for d in digits:
        translated = set()
        for s in d:
            translated.add(translation[s])
        if not translated in valid:
            return False
    return True

def decode(digit, translation):
    global valid
    t = set([translation[s] for s in digit])
    return valid.index(t)

from itertools import permutations

summmmm = 0
for l in a:
    digits = l["digits"]

    eight="abcdefg"
    for perm in permutations(eight):
        translation = {f:t for f,t in zip(eight, perm)}
        if is_valid(translation, digits):
            break

    s = ""
    for d in l["out"]:
        s += str(decode(d, translation))

    print(s)
    summmmm += int(s)

print(summmmm)
