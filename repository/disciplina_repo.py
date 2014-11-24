from domain.disciplina import Disciplina


class DisciplinaRepo():
    """
        Repository pentru discipline
    """

    def __init__(self):
        self.__data = {}

    def add(self, item):

        if item.getID() in self.__data:
            raise ValueError("Discplina existdenta deja")

        self.__data[item.getID()] = item

    def remove(self, id):
        if id in self.__data:
            del self.__data[id]

    def find(self, id):
        if id in self.__data:
            return self.__data[id]

        return None

    def update(self, item):
        if item.getID() in self.__data:
            self.__data[item.getID()] = item
        else:
            raise ValueError("Disciplina inexistenta")

    def getAll(self):
        return self.__data


# # TESTS

def tests():
    d1 = Disciplina(1, "FP", "Georghe")

    repo = DisciplinaRepo()

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


tests()