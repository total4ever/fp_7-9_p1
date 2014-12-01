from domain.disciplina import Disciplina
from domain.student import Student


class Grades():
    def __init__(self, st, disc, grade):
        self.__st = st
        self.__disc = disc
        self.__grade = grade

    def getStudentID(self):
        return self.__st

    def getDisciplinaID(self):
        return self.__disc

    def getGrade(self):
        return self.__grade

# # TESTS

def tests():
    s1 = Student(1, "Paula")
    d1 = Disciplina(1, "FP", "Ion")

    g1 = Grades(1, 1, 10)

    assert g1.getStudentID() == 1
    assert g1.getDisciplinaID() == 1
    assert g1.getGrade() == 10

tests()