class Nota:
    def __init__(self, id_nota, student, disciplina, nota):
        '''
        initializeaza o nota avand un id, un student, o disciplina si o valoare
        :param id_nota: int
        :param student: string
        :param disciplina: string
        :param nota: float
        '''
        self.__id_nota = id_nota
        self.__student = student
        self.__disciplina = disciplina
        self.__nota = nota

    def get_id_nota(self):
        '''
        Returneaza intregul id al unei note
        :return: int
        '''
        return self.__id_nota

    def get_student(self):
        '''
        Returneaza studentul care are nota respectiva
        :return: student
        '''
        return self.__student

    def get_nota(self):
        '''
        Returenaza valoarea reala a notei
        :return: float
        '''
        return self.__nota

    def get_disciplina(self):
        '''
        Returneaza disciplina la care este atribuita nota
        :return: disciplina
        '''
        return self.__disciplina

    def set_nota(self, nota_noua):
        '''
        Seteaza o noua valoare notei
        :param nota_noua: float
        :return: -
        '''
        self.__nota = nota_noua

    def set_student(self, student_nou):
        '''
        Seteaza un nou student notei
        :param student_nou: student
        :return: -
        '''
        self.__student = student_nou

    def set_disciplina(self, disciplina_noua):
        '''
        Seteaza o noua disciplina notei
        :param disciplina_noua: disciplina
        :return: -
        '''
        self.__disciplina = disciplina_noua

    def __eq__(self, other):
        '''
        Verifica daca doua note sunt egale(prin id)
        :param other: note
        :return: True daca id-ul notei self = id-ul notei other
        '''
        return self.__id_nota == other.__id_nota

    def __str__(self):
        '''
        Returneaza un string in care sunt afisate datele notei
        :return: string
        '''
        return f"Nota[{self.__id_nota}]: Student[{self.__student.get_id_student()}] {self.__student.get_nume_student()} : Disciplina[{self.__disciplina.get_id_disciplina()}] {self.__disciplina.get_nume_disciplina()} : Valoarea {self.__nota}"
