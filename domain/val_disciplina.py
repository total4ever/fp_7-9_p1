from domain.disciplina import Disciplina


class DisciplinaValidator():
    """
        Clasa pentru validarea de discipline
    """
    def validate(self, disc):
        errors = []

        if disc.getID() < 0:
            errors.append("ID negativ")

        if disc.getName() == "":
            errors.append("Nume vid")

        if disc.getProf() == "":
            errors.append("Profesor vid")

        if errors != []:
            raise ValueError(errors)

# # TESTS

def tests():
    d1 = Disciplina(-1, "Nume", "Prof")

    val = DisciplinaValidator()

    try:
        val.validate(d1)
        assert False
    except ValueError:
        assert True

    d2 = Disciplina(1, "", "Prof")
    try:
        val.validate(d2)
        assert False
    except ValueError:
        assert True

    d3 = Disciplina(1, "Nume", "")
    try:
        val.validate(d3)
        assert False
    except ValueError:
        assert True

tests()