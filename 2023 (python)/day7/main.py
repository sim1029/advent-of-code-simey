class Hand:
    def __init__(self, hand_str, bid):
        self.hand = self.translate(hand_str)
        self.bid = int(bid)
        self.type = self.calc_type()
        self.original_hand = hand_str

    def __str__(self):
        return f"Hand: {self.hand}, Bid: {self.bid}, Original: {self.original_hand}, Type: {self.type}"

    def __lt__(self, other):
        if self.type == other.type:
            return self.hand < other.hand
        else:
            return self.type < other.type

    def calc_type(self):
        cards = {}
        pairs_set = set()
        jokers = 0
        for char in self.hand:
            if char not in cards:
                cards[char] = 1
            else:
                cards[char] += 1

            if char == "N":
                jokers += 1
            else:
                pairs_set.add(char)
        unique = len(pairs_set)
        most_cards = 1
        for key, val in cards.items():
            if key != "N":
                most_cards = max(most_cards, val)
        most_cards += jokers
        if most_cards >= 5:
            return 1
        elif most_cards == 4:
            return 2
        elif most_cards == 3:
            if unique == 2:
                return 3
            else:
                return 4
        elif most_cards == 2:
            if unique == 3:
                return 5
            else:
                return 6
        else:
            return 7

    def translate(self, hand_str):
        ret = ""
        map = {
            "A": "A",
            "K": "B",
            "Q": "C",
            "J": "N",
            "T": "E",
            "9": "F",
            "8": "G",
            "7": "H",
            "6": "I",
            "5": "J",
            "4": "K",
            "3": "L",
            "2": "M",
        }
        for char in hand_str:
            ret += map[char]
        return ret


with open("input.txt", "r") as file:
    hands = []
    for line in file:
        line = line.strip()
        hand_str, bid = line.split(" ")
        new_hand = Hand(hand_str, bid)
        hands.append(new_hand)
    hands.sort(reverse=True)
    ret = 0
    for i, hand in enumerate(hands):
        rank = i + 1
        ret += rank * hand.bid
    print(ret)
