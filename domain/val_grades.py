class GradesValidator():
    def validate(self, gr):
        errors = []

        if gr.getStudentID() == None:
            errors.append("Student invalid")

        if gr.getDisciplinaID() == None:
            errors.append("Disciplina invalida")

        if gr.getGrade() < 1 or gr.getGrade() > 10:
            errors.append("Nota invalida. [1-10]")

        if errors != []:
            raise ValueError(errors)

