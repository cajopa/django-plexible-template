from plex import *


class DjangoTemplateScanner(Scanner):
    lexicon = Lexicon([
        (Rep(Any(' \t\n')), IGNORE),
    ])
    
    def __init__(self, file, name):
        super().__init__(self.lexicon, ReversibleTextIOWrapper(file), name)
