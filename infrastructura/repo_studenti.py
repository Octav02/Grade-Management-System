from erori.repository_error import RepositoryError


class RepoStudenti:

    def __init__(self):
        '''
        Initializeaza un dictionar de studenti, initial vid
        '''
        self._studenti = {}

    def adauga_student(self, student):
        '''
        Adauga un student in dictionarul de studenti, daca acesta nu exista deja in dictionar
        :param student: student
        :return:-
        :raises: RepositoryError daca id-ul studentului exista deja in dictionar, afisand "Student existent!"
        '''
        if student.get_id_student() in self._studenti:
            raise RepositoryError("Student existent!")
        self._studenti[student.get_id_student()] = student

    def modifica_student(self, student):
        '''
        Inlocuieste studentul din dictionar avand id-ul studentului dat ca parametru, cu acesta din urma
        :param student:  student
        :return: -
        :raises: RepositoryError: Daca id-ul studentului nu se gasesete in dictionarul de studenti, afisand "Student inexistent!"
        '''
        if student.get_id_student() not in self._studenti:
            raise RepositoryError("Student inexistent!")
        self._studenti[student.get_id_student()] = student

    def get_all_studenti(self):
        '''
        Returneaza o lista cu toti studentii din dictionar
        :return: studenti-lista
        '''
        studenti = []
        for id_Student in self._studenti:
            studenti.append(self._studenti[id_Student])
        return studenti

    def cauta_student_dupa_id(self, id_student):
        '''
        Returneaza studentul din dictionar cu id-ul id_student
        :param id_student: int
        :return: student
        :raises:RepositoryError: Daca id-ul studentului nu se gasesete in dictionarul de studenti, afisand "Student inexistent!"
        '''
        if id_student not in self._studenti:
            raise RepositoryError("Student inexistent!")
        return self._studenti[id_student]

    def sterge_student_dupa_id(self, id_student):
        '''
        Sterge studentul din dictionar cu id-ul id_student
        :param id_student: int
        :return: -
        :raises:RepositoryError: Daca id-ul studentului nu se gasesete in dictionarul de studenti, afisand "Student inexistent!"
        '''
        if id_student not in self._studenti:
            raise RepositoryError("Student inexistent!")
        del self._studenti[id_student]


    def __len__(self):
        '''
        Returneaza lungimea dictionarului de studenti
        :return: int
        '''
        return len(self._studenti)
