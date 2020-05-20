OLD_NAMES = ['Rob', 'Robert']

AQ = dict(zip(list('0123456789abcdefghijklmnopqrstuvwxyz'), range(0, 36)))

def aq(text):
    return sum([AQ.get(char, 0) for char in list(text.lower())])

with open('female-first-names.txt') as newNames:
    NEW_NAMES = [name.strip().lower().capitalize()
                 for name in newNames.readlines()]

MATCHES = {}

for oldName in OLD_NAMES:
    oldAq = aq(oldName)
    MATCHES[oldName] = {}
    MATCHES[oldName]['value'] = oldAq
    MATCHES[oldName]['matches'] = []
    for newName in NEW_NAMES:
        #print(newName)
        #print([aq(newName), oldAq])
        if(aq(newName) == oldAq):
            MATCHES[oldName]['matches'].append(newName)

#print(MATCHES)
for matchName in MATCHES:
    match = MATCHES[matchName]
    print(f"{matchName} ({match['value']})")
    print('-' * 20)
    print(f"{', '.join(match['matches'])}")
