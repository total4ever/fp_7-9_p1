from domain.disciplina import Disciplina
from domain.dtos import GradesDTO
from domain.grades import Grades
from domain.student import Student


class GradesRepo():
    def __init__(self):
        self.data = []

    def add(self, grade):
        self.data.append(grade)

    def getAllDTO(self):
        final = []
        for item in self.data:
            x = GradesDTO(item.getStudentID(), item.getDisciplinaID())
            x.setGrade(item.getGrade())
            final.append(x)
        return final

class GradesRepoFile(GradesRepo):
    def __init__(self, fileName):
        GradesRepo.__init__(self)
        self.__file = fileName

        try:
            open(self.__file, "r")
        except FileNotFoundError:
            fH = open(self.__file, "w")
            fH.close()
        self.__readFromFile()


    def __saveToFile(self):
        f = open(self.__file, "w")

        for x in self.data:
            f.write(str(x.getStudentID()) + "|" + str(x.getDisciplinaID()) + "|" + str(x.getGrade()) + "\n")

        f.close()


    def __readFromFile(self):

        self.data = []
        with open(self.__file, "r") as fp:
            for line in fp:
                args = line.split("|")
                x = Grades(int(args[0]), int(args[1]), float(args[2].strip()))
                self.data.append(x)


    def add(self, item):
        GradesRepo.add(self, item)
        self.__saveToFile()


# # TESTS

def tests():
    s1 = Student(1, "Paula")
    d1 = Disciplina(1, "ASC", "Ion")

    repo = GradesRepo()

    g1 = Grades(1, 1, 10)

    repo.add(g1)

    assert len(repo.getAllDTO()) == 1
tests()