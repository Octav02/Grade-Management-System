from domeniu.student import Student
from infrastructura.repo_studenti import RepoStudenti


class RepoStudentiFisier(RepoStudenti):
    def __init__(self, nume_fisier):
        RepoStudenti.__init__(self)
        self.__nume_fisier = nume_fisier

    def __load_from_file(self):
        with open(self.__nume_fisier, "r") as f:
            lines = f.readlines()
            self._studenti.clear()
            for line in lines:
                line = line.strip()
                if line != "\n":
                    params = line.split(";")
                    id_student = int(params[0])
                    nume = params[1]
                    student = Student(id_student, nume)
                    self._studenti[id_student] = student

    def __write_to_file(self):
        with open(self.__nume_fisier, "w") as f:
            for student in self._studenti.values():
                id_student = student.get_id_student()
                nume = student.get_nume_student()
                f.write(str(id_student) + ";" + nume+";\n")

    def adauga_student(self, student):
        self.__load_from_file()
        RepoStudenti.adauga_student(self, student)
        self.__write_to_file()

    def sterge_student_dupa_id(self, id_student):
        self.__load_from_file()
        RepoStudenti.sterge_student_dupa_id(self, id_student)
        self.__write_to_file()

    def modifica_student(self, student):
        self.__load_from_file()
        RepoStudenti.modifica_student(self, student)
        self.__write_to_file()

    def cauta_student_dupa_id(self, id_student):
        self.__load_from_file()
        return RepoStudenti.cauta_student_dupa_id(self, id_student)

    def get_all_studenti(self):
        self.__load_from_file()
        return RepoStudenti.get_all_studenti(self)

    def __len__(self):
        return len(self._studenti)
