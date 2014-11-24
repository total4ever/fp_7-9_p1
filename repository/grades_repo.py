from domain.disciplina import Disciplina
from domain.dtos import GradesDTO
from domain.grades import Grades
from domain.student import Student


class GradesRepo():
    def __init__(self):
        self.__data = []

    def add(self, grade):
        self.__data.append(grade)

    def getAllDTO(self):
        final = []
        for item in self.__data:
            x = GradesDTO(item.getStudent().getID(), item.getDisciplina().getID())
            x.setGrade(item.getGrade())
            final.append(x)
        return final


# # TESTS

def tests():
    s1 = Student(1, "Paula")
    d1 = Disciplina(1, "ASC", "Ion")

    repo = GradesRepo()

    g1 = Grades(s1, d1, 10)

    repo.add(g1)

    assert len(repo.getAllDTO()) == 1


tests()