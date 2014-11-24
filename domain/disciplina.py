class Disciplina():
    """
        Clasa pentru gestionarea de discipline

        Parametrii:
            discID - id disciplina, int
            name - nume disciplina, string
            prof - prof dicisplina, string
    """
    def __init__(self, discID, name, prof):
        self.__discID = discID
        self.__name = name
        self.__prof = prof

    def getID(self):
        return self.__discID

    def getName(self):
        return self.__name

    def getProf(self):
        return self.__prof

    def setName(self, name):
        self.__name = name

    def setProf(self, prof):
        self.__prof = prof

    def __eq__(self, other):
        if other == None:
            return False

        return self.getID() == other.getID()


# # TESTS

def tests():
    d1 = Disciplina(1, "FP", "Ion")

    assert d1.getID() == 1
    assert d1.getName() == "FP"
    assert d1.getProf() == "Ion"

    d1.setName("ASC")
    d1.setProf("Pop")

    assert d1.getName() == "ASC"
    assert d1.getProf() == "Pop"


tests()

