from controller.service_subjects import ServiceDiscipline
from controller.service_grades import ServiceNote
from controller.service_students import ServiceStudenti
from Repository.Repo_grades_files import RepoNoteFisier
from Repository.repo_subjects import RepoDiscipline
from Repository.repo_subjects_files import RepoDisciplineFisier
from Repository.repo_grades import RepoNote
from Repository.repo_students import RepoStudenti
from Repository.repo_students_files import RepoStudentiFisier
from UI.UI import Consola
from Testing.teste import Teste
from Validation.validator_disciplina import ValidatorDisciplina
from Validation.validator_nota import ValidatorNota
from Validation.validator_student import ValidatorStudent
import unittest

if __name__ == '__main__':
    unittest.main(exit=False)
    validator_student = ValidatorStudent()
    validator_disciplina = ValidatorDisciplina()
    validator_nota = ValidatorNota()
    print("1. Ruleaza cu fisiere\n2. Ruleaza cu memorie")
    cmd = int(input(">>>"))
    if cmd == 1:
        repo_studenti = RepoStudentiFisier("studenti.txt")
        repo_discipline = RepoDisciplineFisier("discipline.txt")
        repo_note = RepoNoteFisier("note.txt")
    elif cmd == 2:
        repo_studenti = RepoStudenti()
        repo_discipline = RepoDiscipline()
        repo_note = RepoNote()
    service_studenti = ServiceStudenti(validator_student,repo_studenti)
    service_discipline = ServiceDiscipline(validator_disciplina, repo_discipline)
    service_note = ServiceNote(validator_nota,repo_studenti,repo_discipline,repo_note)
    consola = Consola(service_studenti,service_discipline,service_note)
    consola.runUI()