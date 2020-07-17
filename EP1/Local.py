class Local(object):
    """Classe local"""
    def __init__(self, coord_x, coord_y, frequentadores):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.frequentadores = frequentadores

    def getFrequentadores(self):
        return self.frequentadores