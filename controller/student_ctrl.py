from domain.student import Student
from domain.val_student import StudentValidator
from repository.student_repo import StudentRepo


class StudentCtrl():
    def __init__(self, val, repo):
        self.__val = val
        self.__repo = repo

    def add(self, id, name):
        x = Student(id, name)

        self.__val.validate(x)
        self.__repo.add(x)

    def remove(self, id):
        self.__repo.remove(id)

    def update(self, id, nume):
        x = Student(id, nume)
        self.__repo.update(x)

    def getAll(self):
        return self.__repo.getAll()


# # TESTS

def tests():
    repo = StudentRepo()
    val = StudentValidator()

    ctrl = StudentCtrl(val, repo)

    ctrl.add(1, "Paula")

    assert len(ctrl.getAll()) == 1

    ctrl.add(2, "Paul")
    ctrl.update(2, "Gheorghe")

    x = ctrl.getAll()

    assert x[2].getName() == "Gheorghe"

tests()