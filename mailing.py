from address import Address
class Mailing:
    to_address = Address("132", "miinsk","korola", "56", "99")
    from_address = Address("1328", "minsk","kor", "569", "993")
    cost = 0
    track = 'abc'

    def __init__(self, to_address, from_address, cost, track):
       self.to_address = to_address
       self.from_address = from_address
       self.scost = cost
       self.htrack = track