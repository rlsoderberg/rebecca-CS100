class party:
    def __init__(self, cheena = 'cheena'):
        """
        initialize a party
        """
        
        self.cheena = cheena

    def viddy(self):
        """
        raz to viddy
        """

        print(f'viddy at the {self.cheena}.')

    def spatchko(self, place):
        """
        raz to spatchko

        parameters:
            place (str): a place for spatchko
        """

        print(f'spatchko at the {place}.')

# create a default party
blackstar = party()
# create another party with different properties
low = party('berlin')


print(blackstar.cheena)

# time to party
blackstar.viddy()
blackstar.spatchko('rozz-shop')
