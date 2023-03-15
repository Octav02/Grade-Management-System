from bussiness.service_discipline import ServiceDiscipline
from bussiness.service_note import ServiceNote
from bussiness.service_studenti import ServiceStudenti
from infrastructura.Repo_note_files import RepoNoteFisier
from infrastructura.repo_discipline import RepoDiscipline
from infrastructura.repo_discipline_files import RepoDisciplineFisier
from infrastructura.repo_note import RepoNote
from infrastructura.repo_studenti import RepoStudenti
from infrastructura.repo_studenti_files import RepoStudentiFisier
from prezentare.UI import Consola
from testare.teste import Teste
from validare.validator_disciplina import ValidatorDisciplina
from validare.validator_nota import ValidatorNota
from validare.validator_student import ValidatorStudent
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