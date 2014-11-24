from domain.student import Student


class StudentValidator():
    """
        Clasa pentru validarea de studenti
    """
    def validate(self, st):
        errors = []

        if st.getName() == "":
            errors.append("Nume vid")

        if st.getID() < 0:
            errors.append("ID negativ")

        if errors != []:
            raise ValueError(errors)


# # TESTS

def tests():
    val = StudentValidator()

    s1 = Student(-1, "Paul")

    try:
        val.validate(s1)
        assert False
    except ValueError:
        assert True

    s2 = Student(1, "")

    try:
        val.validate(s2)
        assert False
    except ValueError:
        assert True


tests()