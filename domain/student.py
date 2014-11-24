class Student():
    """
        Clasa pentru gestionarea de studenti

        Parametrii:
            studentID - id student, int
            name - nume, string
    """
    def __init__(self, studentID, name):
        self.__studentID = studentID
        self.__name = name

    def getID(self):
        return self.__studentID

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def __eq__(self, other):
        if other == None:
            return False
        return self.getID() == other.getID()


# # TESTS
def tests():
    s1 = Student(1, "Paul")
    s2 = Student(2, "Paula")
    s3 = Student(1, "Gheroghe")

    assert s1.getID() == 1
    assert s1.getName() == "Paul"

    assert s1 != s2
    assert s1 == s3

tests()
