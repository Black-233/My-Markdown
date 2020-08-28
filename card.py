import collections

Card = collections.namedtuple('card',['number','color'])

class Facard():

    def __init__(self,card):
        self.card = card
    def ret(self,num,col):
        print(self.card(num,col))

card_1 = Facard(Card)
card_1.ret("A","red")
