import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

# FrenchDeck -> 扑克牌
class FrenchDeck:
    # 这里可以生成纸牌的牌面数字
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for rank in self.ranks 
                                       for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

if __name__ == '__main__':
    from random import choice
    
    deck = FrenchDeck()

    # __len__ 方法会直接返回长度
    print(len(deck))
    # __getitem__ 方法会返回切片的值
    print(deck[0])
    # 或者用随机挑模块来随机抽牌
    print(choice(deck.ranks))

