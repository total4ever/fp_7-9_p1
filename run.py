from controller.disciplina_ctrl import DisciplinaCtrl
from controller.grades_ctrl import GradesCtrl
from controller.student_ctrl import StudentCtrl
from domain.val_disciplina import DisciplinaValidator
from domain.val_grades import GradesValidator
from domain.val_student import StudentValidator
from repository.disciplina_repo import DisciplinaRepoFile
from repository.grades_repo import GradesRepoFile
from repository.student_repo import StudentRepoFile
from ui.console import Console

valStudent = StudentValidator()
valDisciplina = DisciplinaValidator()
valGrades = GradesValidator()

repoStudent = StudentRepoFile("stud.txt")
repoDisciplina = DisciplinaRepoFile("disc.txt")
repoGrade = GradesRepoFile("note.txt")

ctrlStudent = StudentCtrl(valStudent, repoStudent)
ctrlDisciplina = DisciplinaCtrl(valDisciplina, repoDisciplina)
ctrlGrades = GradesCtrl(valGrades, repoStudent, repoDisciplina, repoGrade)

console = Console(ctrlStudent, ctrlDisciplina, ctrlGrades)

console.startUI()
