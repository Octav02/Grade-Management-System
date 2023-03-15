from bussiness.service_discipline import ServiceDiscipline
from bussiness.service_note import ServiceNote
from bussiness.service_studenti import ServiceStudenti
from domeniu.disciplina import Disciplina
from domeniu.nota import Nota
from domeniu.student import Student
from erori.repository_error import RepositoryError
from erori.validator_error import ValidatorError
from infrastructura.Repo_note_files import RepoNoteFisier
from infrastructura.repo_discipline import RepoDiscipline
from infrastructura.repo_discipline_files import RepoDisciplineFisier
from infrastructura.repo_note import RepoNote
from infrastructura.repo_studenti import RepoStudenti
from infrastructura.repo_studenti_files import RepoStudentiFisier
from validare.validator_disciplina import ValidatorDisciplina
from validare.validator_nota import ValidatorNota
from validare.validator_student import ValidatorStudent
import unittest


class Teste(unittest.TestCase):

    def __goleste_fisier(self, nume_fisier):
        with open(nume_fisier, "w") as f:
            pass

    def tearDown(self):
        pass

    def teste_domeniu_student(self):
        id_student = 1
        nume_student = "Mihai"
        nume_nou = "Andrei"
        student1 = Student(id_student, nume_student)
        self.assertTrue(1 == 1)
        self.assertTrue(student1.get_id_student() == id_student)
        self.assertEqual(student1.get_nume_student(), nume_student)
        student1.set_nume_student(nume_nou)
        self.assertEqual(student1.get_nume_student(), nume_nou)
        student2 = Student(id_student, nume_student)
        self.assertEqual(student1, student2)

    def teste_domeniu_disicplina(self):
        id_disciplina = 1
        nume_disciplina = "Analiza"
        nume_nou = "Algebra"
        profesor = "Mihai"
        profesor_nou = "Andrei"
        disciplina1 = Disciplina(id_disciplina, nume_disciplina, profesor)
        self.assertEqual(disciplina1.get_id_disciplina(), id_disciplina)
        self.assertEqual(disciplina1.get_nume_disciplina(), nume_disciplina)
        self.assertEqual(disciplina1.get_profesor_disciplina(), profesor)
        disciplina1.set_nume_disciplina(nume_nou)
        disciplina1.set_profesor_disciplina(profesor_nou)
        self.assertEqual(disciplina1.get_nume_disciplina(), nume_nou)
        self.assertEqual(disciplina1.get_profesor_disciplina(), profesor_nou)
        disciplina2 = Disciplina(id_disciplina, nume_disciplina, profesor)
        self.assertEqual(disciplina1, disciplina2)

    def teste_domeniu_note(self):
        id_student1 = 1
        id_student2 = 2
        nume_student = "Mihai"
        nume_nou = "Andrei"
        student1 = Student(id_student1, nume_student)
        student2 = Student(id_student2, nume_nou)

        id_disciplina1 = 1
        id_disciplina2 = 2
        nume_disciplina = "Analiza"
        nume_nou = "Algebra"
        profesor = "Mihai"
        profesor_nou = "Andrei"
        disciplina1 = Disciplina(id_disciplina1, nume_disciplina, profesor)
        disciplina2 = Disciplina(id_disciplina2, nume_nou, profesor_nou)

        id_nota1 = 1
        valoare_nota1 = 6.7
        valoare_nota2 = 7.7
        nota1 = Nota(id_nota1, student1, disciplina1, valoare_nota1)

        self.assertEqual(nota1.get_id_nota(), id_nota1)
        self.assertEqual(nota1.get_nota(), valoare_nota1)
        self.assertEqual(nota1.get_disciplina(), disciplina1)
        self.assertEqual(nota1.get_student(), student1)

        nota1.set_nota(valoare_nota2)
        nota1.set_student(student2)
        nota1.set_disciplina(disciplina2)
        self.assertEqual(nota1.get_nota(), valoare_nota2)
        self.assertEqual(nota1.get_disciplina(), disciplina2)
        self.assertEqual(nota1.get_student(), student2)

        nota2 = Nota(id_nota1, student1, disciplina1, valoare_nota1)
        self.assertEqual(nota1, nota2)

    def teste_validare_student(self):
        validator = ValidatorStudent()
        id_student = 1
        id_invalid = -5
        nume_student = "Mihai"
        nume_invalid = ""
        student1 = Student(id_student, nume_student)
        validator.valideaza(student1)

        student2 = Student(id_invalid, nume_invalid)
        self.assertRaises(ValidatorError,validator.valideaza,student2)

    def teste_validare_disciplina(self):
        validator = ValidatorDisciplina()
        id_disciplina1 = 1
        id_invalid = -22
        nume_disciplina = "Analiza"
        nume_invalid = ""
        profesor = "Mihai"
        profesor_invalid = ""
        disciplina1 = Disciplina(id_disciplina1, nume_disciplina, profesor)
        validator.valideaza(disciplina1)
        disciplina2 = Disciplina(id_invalid, nume_invalid, profesor_invalid)
        self.assertRaises(ValidatorError,validator.valideaza,disciplina2)

    def teste_validare_nota(self):
        validator = ValidatorNota()
        id_student1 = 1
        nume_student = "Mihai"
        student1 = Student(id_student1, nume_student)
        id_disciplina1 = 1
        nume_disciplina = "Analiza"
        profesor = "Mihai"
        disciplina1 = Disciplina(id_disciplina1, nume_disciplina, profesor)
        id_nota = 1
        valoare_nota1 = 6.7
        id_invalid = -25
        valoare_invalida = 0.5
        nota1 = Nota(id_nota, student1, disciplina1, valoare_nota1)
        validator.valideaza(nota1)
        nota2 = Nota(id_invalid, student1, disciplina1, valoare_invalida)
        self.assertRaises(ValidatorError,validator.valideaza,nota2)

    def teste_repo_studenti(self):
        nume_fisier = "testare/test_fisiere.txt"
        repo_studenti = RepoStudentiFisier(nume_fisier)
        self.__goleste_fisier(nume_fisier)
        id_student1 = 1
        id_student2 = 2
        nume_student = "Mihai"
        student1 = Student(id_student1, nume_student)
        nume_nou = "Andrei"
        student2 = Student(id_student2, nume_nou)
        self.assertTrue(len(repo_studenti) == 0)
        repo_studenti.adauga_student(student1)
        self.assertTrue(len(repo_studenti) == 1)

        self.assertRaises(RepositoryError,repo_studenti.adauga_student,student1)
        self.assertRaises(RepositoryError,repo_studenti.modifica_student,student2)
        self.assertRaises(RepositoryError,repo_studenti.cauta_student_dupa_id, id_student2)
        self.assertRaises(RepositoryError,repo_studenti.sterge_student_dupa_id, id_student2)

        student_modificat = Student(id_student1, nume_nou)
        repo_studenti.modifica_student(student_modificat)
        student_cautat = repo_studenti.cauta_student_dupa_id(id_student1)
        self.assertTrue(student_cautat.get_nume_student() == student_modificat.get_nume_student())
        repo_studenti.adauga_student(student2)
        lista_studenti = repo_studenti.get_all_studenti()
        self.assertTrue(len(lista_studenti) == 2)
        repo_studenti.sterge_student_dupa_id(id_student2)
        self.assertTrue(len(repo_studenti) == 1)
        self.assertRaises(RepositoryError, repo_studenti.cauta_student_dupa_id, id_student2)

    def teste_repo_discipline(self):
        nume_fisier = "testare/test_fisiere.txt"
        self.__goleste_fisier(nume_fisier)
        repo_discipline = RepoDisciplineFisier(nume_fisier)
        id_disciplina1 = 1
        id_disciplina2 = 2
        nume_disciplina = "Analiza"
        nume_nou = "Algebra"
        profesor = "Mihai"
        profesor_nou = "Andrei"
        disciplina1 = Disciplina(id_disciplina1, nume_disciplina, profesor)
        disciplina2 = Disciplina(id_disciplina2, nume_nou, profesor_nou)
        self.assertTrue(len(repo_discipline) == 0)
        repo_discipline.adauga_disciplina(disciplina1)
        self.assertTrue(len(repo_discipline) == 1)
        self.assertRaises(RepositoryError,repo_discipline.adauga_disciplina,disciplina1)
        self.assertRaises(RepositoryError,repo_discipline.modifica_disciplina,disciplina2)
        self.assertRaises(RepositoryError,repo_discipline.cauta_disciplina_dupa_id,id_disciplina2)
        self.assertRaises(RepositoryError,repo_discipline.sterge_disciplina_dupa_id,id_disciplina2)

        disciplina_modificata = Disciplina(id_disciplina1, nume_nou, profesor)
        repo_discipline.modifica_disciplina(disciplina_modificata)
        disciplina_cautata = repo_discipline.cauta_disciplina_dupa_id(id_disciplina1)
        self.assertTrue(disciplina_cautata == disciplina_modificata)
        self.assertTrue(disciplina_cautata.get_nume_disciplina() == disciplina_modificata.get_nume_disciplina())
        self.assertTrue(disciplina_cautata.get_profesor_disciplina() == disciplina_modificata.get_profesor_disciplina())

        repo_discipline.adauga_disciplina(disciplina2)
        lista_discipline = repo_discipline.get_all_discipline()
        self.assertTrue(len(lista_discipline) == 2)
        repo_discipline.sterge_disciplina_dupa_id(id_disciplina2)
        self.assertTrue(len(repo_discipline) == 1)
        self.assertRaises(RepositoryError,repo_discipline.cauta_disciplina_dupa_id,id_disciplina2)

    def teste_repo_note(self):
        nume_fisier = "testare/test_fisiere.txt"
        self.__goleste_fisier(nume_fisier)
        repo_note = RepoNoteFisier(nume_fisier)
        id_student1 = 1
        id_student2 = 2
        nume_student = "Mihai"
        nume_nou = "Andrei"
        student1 = Student(id_student1, nume_student)
        student2 = Student(id_student2, nume_nou)

        id_disciplina1 = 1
        id_disciplina2 = 2
        nume_disciplina = "Analiza"
        nume_nou = "Algebra"
        profesor = "Mihai"
        profesor_nou = "Andrei"
        disciplina1 = Disciplina(id_disciplina1, nume_disciplina, profesor)
        disciplina2 = Disciplina(id_disciplina2, nume_nou, profesor_nou)

        id_nota1 = 1
        id_nota2 = 2
        valoare_nota1 = 6.7
        valoare_nota2 = 7.7
        nota1 = Nota(id_nota1, student1, disciplina1, valoare_nota1)
        nota2 = Nota(id_nota2, student1, disciplina2, valoare_nota2)

        self.assertTrue(len(repo_note) == 0)
        repo_note.adauga_nota(nota1)
        self.assertTrue(len(repo_note) == 1)
        self.assertRaises(RepositoryError,repo_note.adauga_nota,nota1)
        self.assertRaises(RepositoryError,repo_note.modifica_nota, nota2)
        self.assertRaises(RepositoryError,repo_note.cauta_nota_dupa_id, id_nota2)
        self.assertRaises(RepositoryError, repo_note.sterge_nota_dupa_id, id_nota2)

        nota_modificata = Nota(id_nota1, student2, disciplina1, valoare_nota2)
        repo_note.modifica_nota(nota_modificata)
        nota_cautata = repo_note.cauta_nota_dupa_id(id_nota1)
        self.assertTrue(nota_cautata == nota_modificata)
        self.assertTrue(nota_cautata.get_student() == nota_modificata.get_student())
        self.assertTrue(nota_cautata.get_disciplina() == nota_modificata.get_disciplina())
        self.assertTrue(nota_cautata.get_nota() == nota_modificata.get_nota())

        repo_note.adauga_nota(nota2)
        lista_note = repo_note.get_all_note()
        self.assertTrue(len(lista_note) == 2)
        repo_note.sterge_nota_dupa_id(id_nota2)
        self.assertTrue(len(repo_note) == 1)
        self.assertRaises(RepositoryError, repo_note.sterge_nota_dupa_id, id_nota2)

    def teste_service_studenti(self):
        nume_fisier = "testare/test_fisiere.txt"
        self.__goleste_fisier(nume_fisier)
        repo_studenti = RepoStudentiFisier(nume_fisier)
        validator = ValidatorStudent()
        id_student1 = 1
        id_invalid = -5
        id_student2 = 2
        nume_student = "Mihai"
        nume_invalid = ""
        nume_nou = "Andrei"
        service_studenti = ServiceStudenti(validator, repo_studenti)
        self.assertTrue(len(repo_studenti) == 0)
        service_studenti.adauga_student(id_student1, nume_student)
        self.assertTrue(len(repo_studenti) == 1)
        self.assertRaises(RepositoryError,service_studenti.adauga_student,id_student1,nume_student)
        self.assertRaises(RepositoryError,service_studenti.modifica_student,id_student2,nume_nou)
        self.assertRaises(RepositoryError,service_studenti.cauta_student_dupa_id,id_student2)
        self.assertRaises(RepositoryError,service_studenti.sterge_student_dupa_id, id_student2)
        self.assertRaises(ValidatorError,service_studenti.adauga_student,id_invalid,nume_invalid)
        self.assertRaises(ValidatorError,service_studenti.modifica_student,id_invalid,nume_invalid)

        service_studenti.modifica_student(id_student1, nume_nou)
        student_cautat = service_studenti.cauta_student_dupa_id(id_student1)
        self.assertTrue(student_cautat.get_id_student() == id_student1)
        self.assertTrue(student_cautat.get_nume_student() == nume_nou)
        service_studenti.adauga_student(id_student2, nume_nou)
        lista_studenti = service_studenti.get_all_studenti()
        self.assertTrue(len(lista_studenti) == 2)
        service_studenti.sterge_student_dupa_id(id_student2)
        self.assertTrue(len(repo_studenti) == 1)
        self.assertRaises(RepositoryError, service_studenti.cauta_student_dupa_id, id_student2)

    def teste_service_discipline(self):
        nume_fisier = "testare/test_fisiere.txt"
        self.__goleste_fisier(nume_fisier)
        repo_discipline = RepoDisciplineFisier(nume_fisier)
        validator = ValidatorDisciplina()
        id_disciplina1 = 1
        id_invalid = -1
        id_disciplina2 = 2
        nume_disciplina = "Analiza"
        nume_invalid = ""
        nume_nou = "Algebra"
        profesor = "Mihai"
        profesor_invalid = ""
        profesor_nou = "Andrei"
        service_discipline = ServiceDiscipline(validator, repo_discipline)
        self.assertTrue(len(repo_discipline) == 0)
        service_discipline.adauga_disciplina(id_disciplina1, nume_disciplina, profesor)
        self.assertTrue(len(repo_discipline) == 1)
        self.assertRaises(RepositoryError,service_discipline.adauga_disciplina,id_disciplina1,nume_disciplina,profesor)
        self.assertRaises(RepositoryError,service_discipline.modifica_disciplina,id_disciplina2,nume_nou,profesor_nou)
        self.assertRaises(RepositoryError,service_discipline.cauta_disciplina_dupa_id, id_disciplina2)
        self.assertRaises(RepositoryError,service_discipline.sterge_disciplina_dupa_id, id_disciplina2)
        self.assertRaises(ValidatorError,service_discipline.adauga_disciplina,id_invalid,nume_invalid,profesor_invalid)
        self.assertRaises(ValidatorError,service_discipline.modifica_disciplina,id_invalid,nume_invalid,profesor_invalid)

        service_discipline.modifica_disciplina(id_disciplina1, nume_disciplina, profesor_nou)
        disciplina_cautata = service_discipline.cauta_disciplina_dupa_id(id_disciplina1)
        self.assertTrue(disciplina_cautata.get_id_disciplina() == id_disciplina1)
        self.assertTrue(disciplina_cautata.get_nume_disciplina() == nume_disciplina)
        self.assertTrue(disciplina_cautata.get_profesor_disciplina() == profesor_nou)
        service_discipline.adauga_disciplina(id_disciplina2, nume_nou, profesor_nou)
        lista_discipline = service_discipline.get_all_discipline()
        self.assertTrue(len(lista_discipline) == 2)
        service_discipline.sterge_disciplina_dupa_id(id_disciplina2)
        self.assertTrue(len(repo_discipline) == 1)
        self.assertRaises(RepositoryError,service_discipline.cauta_disciplina_dupa_id, id_disciplina2)

    def teste_service_note(self):
        nume_fisier1 = "testare/test_fisiere1.txt"
        self.__goleste_fisier(nume_fisier1)
        repo_studenti = RepoStudentiFisier(nume_fisier1)
        validator = ValidatorNota()
        id_student1 = 1
        id_student2 = 2
        nume_student = "Mihai"
        nume_invalid = ""
        nume_nou = "Andrei"

        nume_fisier2 = "testare/test_fisiere2.txt"
        self.__goleste_fisier(nume_fisier2)
        repo_discipline = RepoDisciplineFisier(nume_fisier2)
        id_disciplina1 = 1
        id_invalid = -1
        id_disciplina2 = 2
        nume_disciplina = "Analiza"
        nume_nou = "Algebra"
        profesor = "Mihai"
        profesor_invalid = ""
        profesor_nou = "Andrei"
        student1 = Student(id_student1, nume_student)
        student2 = Student(id_student2, nume_nou)
        disciplina1 = Disciplina(id_disciplina1, nume_disciplina, profesor)
        disciplina2 = Disciplina(id_disciplina2, nume_nou, profesor_nou)

        repo_studenti.adauga_student(student1)
        repo_studenti.adauga_student(student2)
        repo_discipline.adauga_disciplina(disciplina1)
        repo_discipline.adauga_disciplina(disciplina2)

        nume_fisier = "testare/test_fisiere.txt"
        self.__goleste_fisier(nume_fisier)
        repo_note = RepoNoteFisier(nume_fisier)
        id_nota1 = 1
        id_nota2 = 2
        valoare_nota1 = 6.7
        valoare_nota2 = 7.7
        valoare_invalida = 0.5
        service_note = ServiceNote(validator, repo_studenti, repo_discipline, repo_note)
        self.assertTrue(len(repo_note) == 0)
        service_note.adauga_nota(id_nota1, id_student1, id_disciplina1, valoare_nota1)
        self.assertTrue(len(repo_note) == 1)
        self.assertRaises(RepositoryError,service_note.adauga_nota,id_nota1, id_student1, id_disciplina1, valoare_nota1)
        self.assertRaises(RepositoryError,service_note.modifica_nota,id_nota2, id_student1, id_disciplina1, valoare_nota1)
        self.assertRaises(RepositoryError,service_note.cauta_nota_dupa_id,id_nota2)
        self.assertRaises(RepositoryError,service_note.sterge_nota_dupa_id,id_nota2)
        self.assertRaises(ValidatorError,service_note.adauga_nota,id_invalid, id_student1, id_disciplina1, valoare_invalida)
        self.assertRaises(ValidatorError,service_note.modifica_nota,id_invalid, id_student1, id_disciplina1, valoare_invalida)

        service_note.modifica_nota(id_nota1, id_student2, id_disciplina2, valoare_nota2)
        nota_cautata = service_note.cauta_nota_dupa_id(id_nota1)
        self.assertTrue(nota_cautata.get_id_nota() == id_nota1)
        self.assertTrue(nota_cautata.get_student() == student2)
        self.assertTrue(nota_cautata.get_nota() == valoare_nota2)
        self.assertTrue(nota_cautata.get_disciplina() == disciplina2)
        service_note.adauga_nota(id_nota2, id_student2, id_disciplina2, valoare_nota2)
        lista_note = service_note.get_all_note()
        self.assertTrue(len(lista_note) == 2)
        service_note.sterge_nota_dupa_id(id_nota1)
        self.assertTrue(len(repo_note) == 1)
        self.assertRaises(RepositoryError,service_note.cauta_nota_dupa_id,id_nota1)
        service_note.adauga_nota(id_nota1, id_student1, id_disciplina1, valoare_nota1)
        self.assertTrue(len(repo_note) == 2)
        self.assertTrue(len(repo_discipline) == 2)
        self.assertTrue(len(repo_studenti) == 2)
        service_note.sterge_student_si_note(id_student1)
        self.assertTrue(len(repo_note) == 1)
        self.assertTrue(len(repo_discipline) == 2)
        self.assertTrue(len(repo_studenti) == 1)
        self.assertRaises(RepositoryError,service_note.cauta_nota_dupa_id,id_nota1)
        self.assertRaises(RepositoryError,repo_studenti.cauta_student_dupa_id,id_student1)

        service_note.sterge_disciplina_si_note(id_disciplina2)
        self.assertTrue(len(repo_note) == 0)
        self.assertTrue(len(repo_discipline) == 1)
        self.assertTrue(len(repo_studenti) == 1)
        self.assertRaises(RepositoryError,service_note.cauta_nota_dupa_id,id_nota2)
        self.assertRaises(RepositoryError,repo_discipline.cauta_disciplina_dupa_id,id_disciplina2)

        service_note.sterge_student_si_note(id_student2)
        service_note.sterge_disciplina_si_note(id_disciplina1)

        student_aux1 = Student(1, "Mihai")
        repo_studenti.adauga_student(student_aux1)
        student_aux2 = Student(2, "Andrei")
        repo_studenti.adauga_student(student_aux2)
        student_aux3 = Student(3, "Bogdan")
        repo_studenti.adauga_student(student_aux3)
        student_aux4 = Student(4, "Irina")
        repo_studenti.adauga_student(student_aux4)
        student_aux5 = Student(5, "Anda")
        repo_studenti.adauga_student(student_aux5)
        student_aux6 = Student(6, "Andreea")
        repo_studenti.adauga_student(student_aux6)
        disciplina_aux1 = Disciplina(1, "Analiza", "Mihai")
        repo_discipline.adauga_disciplina(disciplina_aux1)
        disciplina_aux2 = Disciplina(2, "Algebra", "Andrei")
        repo_discipline.adauga_disciplina(disciplina_aux2)
        nota_aux1 = Nota(1, student_aux1, disciplina_aux1, 10)
        repo_note.adauga_nota(nota_aux1)
        nota_aux2 = Nota(2, student_aux2, disciplina_aux1, 9)
        repo_note.adauga_nota(nota_aux2)
        nota_aux3 = Nota(3, student_aux3, disciplina_aux2, 8)
        repo_note.adauga_nota(nota_aux3)
        nota_aux4 = Nota(4, student_aux1, disciplina_aux2, 9)
        repo_note.adauga_nota(nota_aux4)

        sefi_promotie = service_note.get_sefi_promotie()
        self.assertTrue(len(sefi_promotie) == 0)
        nota_aux5 = Nota(5, student_aux4, disciplina_aux2, 6)
        repo_note.adauga_nota(nota_aux5)
        nota_aux6 = Nota(6, student_aux5, disciplina_aux1, 7)
        repo_note.adauga_nota(nota_aux6)
        nota_aux7 = Nota(7, student_aux6, disciplina_aux1, 8)
        repo_note.adauga_nota(nota_aux7)
        nota_aux8 = Nota(8, student_aux6, disciplina_aux1, 6)
        repo_note.adauga_nota(nota_aux8)
        sefi_promotie = service_note.get_sefi_promotie()
        self.assertTrue(len(sefi_promotie) == 1)
        self.assertTrue(sefi_promotie[0].get_nume() == "Mihai")
        self.assertTrue(sefi_promotie[0].get_medie() == 9.5)

        lista_studenti = service_note.get_studenti_note_de_la_disciplina(1)
        self.assertTrue(len(lista_studenti) == 4)
        self.assertTrue(lista_studenti[0].get_nume() == "Anda")
