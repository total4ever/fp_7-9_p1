from pip._vendor.requests.packages.chardet.jpcntx import MAX_REL_THRESHOLD
from domain.disciplina import Disciplina
from domain.grades import Grades
from domain.student import Student
from domain.val_grades import GradesValidator
from repository.disciplina_repo import DisciplinaRepo
from repository.grades_repo import GradesRepo
from repository.student_repo import StudentRepo
from math import ceil

class GradesCtrl():
    def __init__(self, val, studRepo, discRepo, gradeRepo):
        self.__val = val
        self.__studRepo = studRepo
        self.__discRepo = discRepo
        self.__gradeRepo = gradeRepo

    def add(self, studentID, disciplinaID, grade):
        st = self.__studRepo.find(studentID)
        disc = self.__discRepo.find(disciplinaID)

        g = Grades(st, disc, grade)

        self.__val.validate(g)
        self.__gradeRepo.add(g)

    def discStudentGrades(self, discID):
        all = self.__gradeRepo.getAllDTO()

        final = []

        for item in all:
            if item.getDiscID() == discID:

                poz = -1

                for i in range(len(final)):
                    if final[i].getStudID() == item.getStudID():
                        poz = i

                if poz == -1:
                    x = item
                    x.addGrade(item.getGrade())
                    final.append(x)
                else:
                    final[poz].addGrade(item.getGrade())

        for i in range(len(final)):
            #print(final[i].getDiscID())

            final[i].setStudName(self.__studRepo.find(final[i].getStudID()).getName())

        ordered = sorted(final, key=lambda x: x.getStudName(), reverse=True)

        return final

    def studentsByAvg(self):
        all = self.__gradeRepo.getAllDTO()

        final = []
        for item in all:
            poz = -1

            for i in range(len(final)):
                if final[i].getStudID() == item.getStudID():
                    poz = i

            if poz == -1:
                x = item
                x.addGrade(item.getGrade())
                final.append(x)
            else:
                final[poz].addGrade(item.getGrade())

        for i in range(len(final)):
            final[i].setStudName(self.__studRepo.find(final[i].getStudID()).getName())

        ordered = sorted(final, key=lambda x: x.getAvg(), reverse=True)

        proc = ceil(0.2*len(ordered))
        return ordered[:proc]

# # TESTS

def tests():
    val = GradesValidator()
    studRepo = StudentRepo()
    discRepo = DisciplinaRepo()
    gradeRepo = GradesRepo()

    ctrl = GradesCtrl(val, studRepo, discRepo, gradeRepo)


    studRepo.add(Student(1, "Paul"))
    studRepo.add(Student(2, "Paula"))
    studRepo.add(Student(3, "Gheorghe"))

    discRepo.add(Disciplina(1, "FP", "Ion"))
    discRepo.add(Disciplina(2, "ASC", "Ion"))
    discRepo.add(Disciplina(3, "LC", "Ion"))
    discRepo.add(Disciplina(4, "Mate", "Ion"))

    ctrl.add(1, 2, 10)
    ctrl.add(1, 2, 8)
    ctrl.add(1, 1, 8)

    ctrl.add(2, 2, 10)

    ctrl.add(3, 2, 10)


    lista = ctrl.discStudentGrades(2)

    assert lista[0].getStudName() == "Paul"
    assert lista[0].getGrades() == [10, 8]

    assert lista[1].getStudName() == "Paula"
    assert lista[1].getGrades() == [10]

    assert lista[2].getStudName() == "Gheorghe"
    assert lista[2].getGrades() == [10]

    lista2 = ctrl.studentsByAvg()

    assert lista2[0].getStudName() == "Paula"
    assert lista2[0].getAvg() == 10.0

    #assert lista2[1].getStudName() == "Gheorghe"
    #assert lista2[1].getAvg() == 10.0

    #assert lista2[2].getStudName() == "Paul"
    #assert lista2[2].getAvg() == (10+8+8)/3

tests()