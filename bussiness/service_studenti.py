from domeniu.student import Student
import random

class ServiceStudenti:
    def __init__(self, validator_student, repo_studenti):
        '''
        Initializeaza service-ul de studenti cu un validator de student si un repository de studenti
        :param validator_student: validator
        :param repo_studenti: repository
        '''
        self.__validator_student = validator_student
        self.__repo_studenti = repo_studenti

    def adauga_student(self, id_student, nume_student):
        '''
        Creeaza un student cu parametrii dati, il valideaza si daca e valid il adauga in dictionar
        :param id_student: int
        :param nume_student: string
        :return: -
        :raises: RepositoryError daca id-ul studentului exista deja in dictionar, afisand "Student existent!"
                 ValidatorError: daca id-ul <= 0, atunci concateneaza mesajul "id invalid!\n"
                                 daca numele este vid, atunci concateneaza mesajul "nume invalid!\n"
        '''
        student = Student(id_student, nume_student)
        self.__validator_student.valideaza(student)
        self.__repo_studenti.adauga_student(student)

    def modifica_student(self, id_student, nume_student):
        '''
        Creeaza un student cu parametrii dati, il valideaza si daca e valid inlocuieste
        studentul din dicitonar cu id-ul id_student cu studentul nou creat
        :param id_student: int
        :param nume_student: string
        :return:-
        :raises: RepositoryError: Daca id-ul studentului nu se gasesete in dictionarul de studenti, afisand "Student inexistent!"
                  ValidatorError: daca id-ul <= 0, atunci concateneaza mesajul "id invalid!\n"
                                 daca numele este vid, atunci concateneaza mesajul "nume invalid!\n"

        '''
        student = Student(id_student, nume_student)
        self.__validator_student.valideaza(student)
        self.__repo_studenti.modifica_student(student)

    def get_all_studenti(self):
        '''
        Returneaza o lista cu toti studentii din dictionar
        :return: studenti-lista
        '''
        return self.__repo_studenti.get_all_studenti()

    def cauta_student_dupa_id(self, id_student):
        '''
        Returneaza studentul din dictionar cu id-ul id_student
        :param id_student: int
        :return: student
        :raises:RepositoryError: Daca id-ul studentului nu se gasesete in dictionarul de studenti, afisand "Student inexistent!"
        '''
        return self.__repo_studenti.cauta_student_dupa_id(id_student)

    def creeaza_si_adauga_student(self):
        '''
        Creeaza un student random si il adauga la lista de studenti
        :return:-
        '''
        id = random.randint(1,100000000001)
        lista_nume = ["Andrei","Bogdan","Cristi", "Constantin","Codrut","Mihnea", "Octav", "Alexandra", "Casiana", "Matei",
                      "Darius", "Daria", "Minodora", "Tudor", "Emanuela", "Elena", "Andreea", "Mihai"]
        id_nume = random.randint(0,len(lista_nume)-1)
        nume = lista_nume[id_nume]
        self.adauga_student(id, nume)

    def sterge_student_dupa_id(self, id_student):
        '''
        Sterge studentul din dictionar cu id-ul id_student
        :param id_student: int
        :return: -
        :raises:RepositoryError: Daca id-ul studentului nu se gasesete in dictionarul de studenti, afisand "Student inexistent!"
        '''
        self.__repo_studenti.sterge_student_dupa_id(id_student)
