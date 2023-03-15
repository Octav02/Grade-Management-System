class Student:
    def __init__(self, id_student, nume_student):
        '''
        Initializeaza un student avand un id si un nume
        :param id_student: int
        :param nume_student: string
        '''
        self.__id_student = id_student
        self.__nume_student = nume_student

    def get_id_student(self):
        '''
        Returneaza id-ul intreg al unui student
        :return: int
        '''
        return self.__id_student

    def get_nume_student(self):
        '''
        Returneaza numele string al unui student
        :return: string
        '''
        return self.__nume_student

    def set_nume_student(self, nume_nou):
        '''
        Seteaza numele string al unui student
        :param nume_nou: string
        :return: -
        '''
        self.__nume_student =  nume_nou

    def __eq__(self, other):
        '''
        Verifica daca doi studenti sunt egali(prin id)
        :param other: student
        :return: True daca id-ul studentului self = id-ul studentului other
                 False altfel
        '''
        return self.__id_student == other.__id_student

    def __str__(self):
        '''
        Returneaza un string continand toate datele studentului
        :return: string
        '''
        return f"Studentul [{self.__id_student}]: Nume : {self.__nume_student}"
