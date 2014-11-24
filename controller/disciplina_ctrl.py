from domain.disciplina import Disciplina
from domain.val_disciplina import DisciplinaValidator
from repository.disciplina_repo import DisciplinaRepo


class DisciplinaCtrl():
    def __init__(self, val, repo):
        self.__val = val
        self.__repo = repo

    def add(self, id, name, prof):
        x = Disciplina(id, name, prof)

        self.__val.validate(x)
        self.__repo.add(x)

    def remove(self, id):
        self.__repo.remove(id)

    def update(self, id, nume, prof):
        x = Disciplina(id, nume, prof)
        self.__repo.update(x)

    def getAll(self):
        return self.__repo.getAll()


# # TESTS

def tests():
    repo = DisciplinaRepo()
    val = DisciplinaValidator()

    ctrl = DisciplinaCtrl(val, repo)

    ctrl.add(1, "FP", "Ion")

    assert len(ctrl.getAll()) == 1

    ctrl.add(2, "ASC", "Vancea")
    ctrl.update(2, "ASC", "Anca")

    x = ctrl.getAll()

    assert x[2].getProf() == "Anca"


tests()