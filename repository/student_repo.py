from domain.student import Student


class StudentRepo():
    """
        Repository pentru studenti
    """

    def __init__(self):
        self.data = {}

    def add(self, item):

        if item.getID() in self.data:
            raise ValueError("Student existdent deja")

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
            raise ValueError("Student inexistent")

    def getAll(self):
        return self.data


class StudentRepoFile(StudentRepo):
    def __init__(self, fileName):
        StudentRepo.__init__(self)
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
            f.write(str(x.getID()) + "|" + x.getName() + "\n")

        f.close()


    def __readFromFile(self):

        self.data = {}
        with open(self.__file, "r") as fp:
            for line in fp:
                args = line.split("|")
                x = Student(int(args[0]), args[1])
                self.data[x.getID()] = x


    def add(self, item):
        StudentRepo.add(self, item)
        self.__saveToFile()

    def remove(self, ID):
        StudentRepo.remove(self, ID)
        self.__saveToFile()

    def update(self, item):
        StudentRepo.update(self, item)
        self.__saveToFile()

# # TESTS

def tests():
    s1 = Student(1, "Paula")

    repo = StudentRepo()

    repo.add(s1)
    assert len(repo.getAll()) == 1

    x = repo.find(1)
    assert x.getName() == "Paula"

    s2 = Student(1, "Paula")

    try:
        repo.add(s2)
        assert False
    except ValueError:
        assert True

    s3 = Student(3, "Paul")

    repo.add(s3)
    assert len(repo.getAll()) == 2

    repo.update(Student(3, "Gheorghe"))
    assert repo.find(3).getName() == "Gheorghe"

    repo.remove(3)
    assert len(repo.getAll()) == 1


#tests()