names = ['A'] + [str(n) for n in range(2,11)] + ['J', 'Q', 'K']

def generateSuit():
    return [card for card in range(13)]

def namedList(cards):
    return [names[card] for card in cards]

if __name__ == '__main__':
    print(namedList(generateSuit()))