__author__ = 'lawrencechen'


class PrimeNode(object):
    def __init__(self):
        pass


class PrimeLeafNode(PrimeNode):
    def __init__(self):
        super(PrimeLeafNode, self).__init__()


class PrimeIndexNode(PrimeNode):
    def __init__(self):
        super(PrimeIndexNode, self).__init__()


class PrimeDigitTrie(object):
    def __init__(self, levels):
        self._root = PrimeLeafNode() if levels == 1 else PrimeIndexNode()
