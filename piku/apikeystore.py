keys = {
    'pete':'28054D5C-83D9-41E7-BF71-FD2D7FDFDC87',
    'test':'4AFC5337-3BCF-4E1D-847E-5F0FA14A7204'
}
class APIKeystore(object):
    def __init__(self):
        pass

    def key(self,username):
        return keys[username]