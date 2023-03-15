from domeniu.disciplina import Disciplina
from domeniu.nota import Nota
from domeniu.student import Student
from infrastructura.repo_note import RepoNote


class RepoNoteFisier(RepoNote):
    def __init__(self, nume_fisier):
        RepoNote.__init__(self)
        self.__nume_fisier = nume_fisier

    def __load_from_file(self):
        with open(self.__nume_fisier,"r") as f:
            lines = f.readlines()
            self._note.clear()
            for line in lines:
                line.strip("")
                if line != "":
                    params = line.split(";")
                    id_nota = int(params[0])
                    id_student = int(params[1])
                    nume_student = params[2]
                    id_disciplina = int(params[3])
                    nume_disciplina = params[4]
                    profesor_disciplina = params[5]
                    valoare_nota = float(params[6])
                    student = Student(id_student, nume_student)
                    disciplina = Disciplina(id_disciplina, nume_disciplina, profesor_disciplina)
                    nota = Nota(id_nota,student,disciplina,valoare_nota)
                    self._note[id_nota] = nota
    def __write_to_file(self):
        with open(self.__nume_fisier,"w") as f:
            for nota in self._note.values():
                student = nota.get_student()
                disciplina = nota.get_disciplina()
                valoare_nota = nota.get_nota()
                id_nota = nota.get_id_nota()
                id_student = student.get_id_student()
                nume_student = student.get_nume_student()
                id_disciplina = disciplina.get_id_disciplina()
                nume_disciplina = disciplina.get_nume_disciplina()
                profesor_disciplina = disciplina.get_profesor_disciplina()
                f.write(str(id_nota)+";"+str(id_student)+";"+nume_student+";"+str(id_disciplina)+";"+nume_disciplina+";"+profesor_disciplina+";"+str(valoare_nota)+";\n")

    def adauga_nota(self, nota):
        self.__load_from_file()
        RepoNote.adauga_nota(self,nota)
        self.__write_to_file()

    def modifica_nota(self, nota):
        self.__load_from_file()
        RepoNote.modifica_nota(self,nota)
        self.__write_to_file()

    def sterge_nota_dupa_id(self, id_nota):
        self.__load_from_file()
        RepoNote.sterge_nota_dupa_id(self,id_nota)
        self.__write_to_file()

    def cauta_nota_dupa_id(self, id_nota):
        self.__load_from_file()
        return RepoNote.cauta_nota_dupa_id(self,id_nota)

    def get_all_note(self):
        self.__load_from_file()
        return RepoNote.get_all_note(self)

    def __len__(self):
        self.__load_from_file()
        return len(self._note)