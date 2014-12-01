from domain.disciplina import Disciplina


class DisciplinaRepo():
    """
        Repository pentru discipline
    """

    def __init__(self):
        self.data = {}

    def add(self, item):

        if item.getID() in self.data:
            raise ValueError("Discplina existdenta deja")

        self.data[item.getID()] = item

    def remove(self, id):
        if id in self.data:
            del self.data[id]

    def find(self, id):
        if id in self.data:
            return self.data[id]

        return None

    def update(self, item):
        if item.getID() in self.data:
            self.data[item.getID()] = item
        else:
            raise ValueError("Disciplina inexistenta")

    def getAll(self):
        return self.data


class DisciplinaRepoFile(DisciplinaRepo):
    def __init__(self, fileName):
        DisciplinaRepo.__init__(self)
        self.__file = fileName

        try:
            open(self.__file, "r")
        except FileNotFoundError:
            fH = open(self.__file, "w")
            fH.close()
        self.__readFromFile()


    def __saveToFile(self):
        f = open(self.__file, "w")

        for e in self.data:
            x = self.data[e]
            f.write(str(x.getID()) + "|" + x.getName() + "|" + x.getProf() + "\n")

        f.close()


    def __readFromFile(self):

        self.data = {}
        with open(self.__file, "r") as fp:
            for line in fp:
                args = line.split("|")
                x = Disciplina(int(args[0]), args[1], args[2].strip())
                self.data[x.getID()] = x


    def add(self, item):
        DisciplinaRepo.add(self, item)
        self.__saveToFile()

    def remove(self, ID):
        DisciplinaRepo.remove(self, ID)
        self.__saveToFile()

    def update(self, item):
        DisciplinaRepo.update(self, item)
        self.__saveToFile()

# # TESTS

def tests():
    d1 = Disciplina(1, "FP", "Georghe")

    repo = DisciplinaRepoFile("disc.txt")

    repo.add(d1)
    assert len(repo.getAll()) == 1

    x = repo.find(1)
    assert x.getName() == "FP"

    d2 = Disciplina(1, "FP", "Ceva")

    try:
        repo.add(d2)
        assert False
    except ValueError:
        assert True

    d3 = Disciplina(3, "ASC", "Vancea")

    repo.add(d3)
    assert len(repo.getAll()) == 2

    repo.update(Disciplina(3, "ASC", "Anca"))
    assert repo.find(3).getProf() == "Anca"

    repo.remove(3)
    assert len(repo.getAll()) == 1


#tests()