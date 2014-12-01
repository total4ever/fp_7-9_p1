class Console():
    def __init__(self, ctrlStudent, ctrlDisc, ctrlGrades):
        self.__ctrlStudent = ctrlStudent
        self.__ctrlDisc = ctrlDisc
        self.__ctrlGrades = ctrlGrades

    def __meniu(self):
        print("1 - Adauga student")
        print("2 - Afisare studenti")

        print("3 - Adauga disciplina")
        print("4 - Afisare discipline")

        print("5 - Modifica student")
        print("6 - Sterge student")

        print("7 - Modifica disciplina")
        print("8 - Sterge disciplina")

        print("9 - Adauga nota")

        print("note - Afiseaza studentii cu notele la o disciplina")
        print("medii - Medile studentilor la toate materile")

    def __cmd(self):
        return input("Comanda: ")

    def __adaugaStudent(self):
        id = int(input("ID student: "))
        name = input("Nume student: ")

        try:
            self.__ctrlStudent.add(id, name)
        except ValueError as msg:
            print(msg)

    def __afiseazaStudenti(self):
        lista = self.__ctrlStudent.getAll()

        for item in lista:
            x = lista[item]
            print(x.getID(), ":", x.getName())

    def __adaugaDisciplina(self):
        id = int(input("ID disciplina: "))
        nume = input("Nume: ")
        prof = input("Prof: ")

        try:
            self.__ctrlDisc.add(id, nume, prof)
        except ValueError as msg:
            print(msg)

    def __afiseazaDiscipline(self):
        lista = self.__ctrlDisc.getAll()

        for item in lista:
            x = lista[item]
            print(x.getID(), ":", x.getName(), x.getProf())

    def __modificaStudent(self):
        id = int(input("ID student: "))
        nume = input("Nume nou: ")

        self.__ctrlStudent.update(id, nume)

    def __stergeStudent(self):
        id = int(input("ID student: "))

        self.__ctrlStudent.remove(id)

    def __modificaDisciplina(self):
        id = int(input("ID disciplina: "))
        nume = input("Nume nou: ")
        prof = input("Prof nou: ")

        self.__ctrlDisc.update(id, nume, prof)

    def __stergeDisciplina(self):
        id = int(input("ID disciplina: "))

        self.__ctrlDisc.remove(id)

    def __adaugaNota(self):
        studentID = int(input("ID Student: "))
        discID = int(input("ID Disciplina: "))
        nota = float(input("Nota: "))

        try:
            self.__ctrlGrades.add(studentID, discID, nota)
        except ValueError as msg:
            print(msg)

    def __noteLaDisciplina(self):
        discID = int(input("ID Disciplina: "))
        lista = self.__ctrlGrades.discStudentGrades(discID)

        for x in lista:
            print(x.getStudName(), x.getGrades())

    def __mediiStudenti(self):
        lista = self.__ctrlGrades.studentsByAvg()

        for x in lista:
            print(x.getStudName(), x.getAvg())

    def startUI(self):
        # self.__ctrlStudent.add(1, "Paul")
        # self.__ctrlStudent.add(2, "Ana")
        # self.__ctrlStudent.add(3, "Gheorghe")
        # self.__ctrlStudent.add(4, "Paula")
        # self.__ctrlStudent.add(5, "Maria")
        #
        # self.__ctrlDisc.add(1, "FP", "Prof 1")
        # self.__ctrlDisc.add(2, "ASC", "Prof 2")
        # self.__ctrlDisc.add(3, "Analiza", "Prof 3")
        # self.__ctrlDisc.add(4, "Algebra", "Prof 4")
        # self.__ctrlDisc.add(5, "Logica Comp.", "Prof 5")
        #
        # self.__ctrlGrades.add(1, 1, 10)
        # self.__ctrlGrades.add(1, 1, 9)
        # self.__ctrlGrades.add(1, 1, 9.5)
        # self.__ctrlGrades.add(1, 1, 10)
        #
        # self.__ctrlGrades.add(1, 2, 8)
        # self.__ctrlGrades.add(1, 3, 8.5)
        #
        # self.__ctrlGrades.add(2, 3, 10)
        # self.__ctrlGrades.add(2, 4, 5)
        #
        #
        # self.__ctrlGrades.add(3, 5, 6.34)
        # self.__ctrlGrades.add(3, 4, 7)
        #
        # self.__ctrlGrades.add(4, 4, 8.5)
        # self.__ctrlGrades.add(4, 4, 9.9)
        # self.__ctrlGrades.add(4, 3, 10)
        #
        # self.__ctrlGrades.add(5, 5, 8.30)
        # self.__ctrlGrades.add(5, 1, 10)
        # self.__ctrlGrades.add(5, 1, 7.60)

        while True:
            self.__meniu()
            cmd = self.__cmd()

            if cmd == "1":
                self.__adaugaStudent()
            if cmd == "2":
                self.__afiseazaStudenti()
            if cmd == "3":
                self.__adaugaDisciplina()
            if cmd == "4":
                self.__afiseazaDiscipline()
            if cmd == "5":
                self.__modificaStudent()
            if cmd == "6":
                self.__stergeStudent()
            if cmd == "7":
                self.__modificaDisciplina()
            if cmd == "8":
                self.__stergeDisciplina()
            if cmd == "9":
                self.__adaugaNota()

            if cmd == "note":
                self.__noteLaDisciplina()
            if cmd == "medii":
                self.__mediiStudenti()