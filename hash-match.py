import hashlib
import json

def hashName (algorithm, name):
    h = hashlib.new(algorithm)
    h.update(name.encode('utf-8'))
    if algorithm == 'shake_128':
        return h.hexdigest(128)
    elif algorithm == 'shake_256':
        return h.hexdigest(256)
    return h.hexdigest()

def matchLength(a, b):
    length = 0
    for i in range(0, len(a)):
        if a[i] == b[i]:
            length += 1
        else:
            break
    return length

OLD_NAMES = ['rob', 'robert']

with open('female-first-names.txt') as newNames:
    NEW_NAMES = [name.strip().lower()
                 for name in newNames.readlines()]

MIN_MATCH = 3

matches = {}


for algorithm in hashlib.algorithms_available:
    for oldName in OLD_NAMES:
        oldNameHash = hashName(algorithm, oldName)
        for newName in NEW_NAMES:
            if newName == oldName:
                continue
            newNameHash = hashName(algorithm, newName)
            length = matchLength(oldNameHash, newNameHash)
            if length >= MIN_MATCH:
                # Create everything lazily so we don't end up with empty fields
                matches.setdefault(algorithm, {})\
                    .setdefault((oldName, oldNameHash), {})\
                    .setdefault(length, [])\
                    .append((newName, newNameHash))


#print(matches)
# We now use non-string keys, so this doesn't work
#print(json.dumps(matches, indent=4, sort_keys=True))

# Sort keys for stability of output, they are not given alphabetically sorted
# and the order varies between runs
for algorithm in sorted(matches.keys()):
    print(f'### {algorithm}')
    for oldName in sorted(matches[algorithm].keys()):
        print(f'\n#### {": ".join(oldName)}')
        lengths = matches[algorithm][oldName]
        for length in sorted(lengths.keys()):
            print(f'\n##### {length}\n')
            for newName in lengths[length]:
                print(f'{": ".join(newName)}\n')
