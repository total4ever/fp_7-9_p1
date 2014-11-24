class GradesDTO():
    def __init__(self, idStud, idDisc):
        self.__idStud = idStud
        self.__idDisc = idDisc

        self.__grade = 0

        self.__grades = []
        self.__discName = ""
        self.__studName = ""

    def getStudID(self):
        return self.__idStud

    def getDiscID(self):
        return self.__idDisc

    def addGrade(self, grade):
        self.__grades.append(grade)

    def setStudName(self, name):
        self.__studName = name

    def getStudName(self):
        return self.__studName

    def setGrade(self, grade):
        self.__grade = grade

    def getGrade(self):
        return self.__grade

    def getGrades(self):
        self.__grades.sort(reverse=True)
        return self.__grades

    def getAvg(self):
        if len(self.__grades) > 0:
            total = 0
            for nota in self.__grades:
                total += nota

            return total / len(self.__grades)

        return 0.0
