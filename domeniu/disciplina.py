class Disciplina:
    def __init__(self, id_disciplina, nume_disciplina, profesor_disciplina):
        '''
        Initializeaza o disciplina avand un id, un nume si un profesor
        :param id_disciplina: int
        :param nume_disciplina: string
        :param profesor_disciplina: string
        '''
        self.__id_disciplina = id_disciplina
        self.__nume_disciplina = nume_disciplina
        self.__profesor_disciplina = profesor_disciplina

    def get_id_disciplina(self):
        '''
        Returneaza id-ul intreg al disciplinei
        :return: int
        '''
        return self.__id_disciplina

    def get_nume_disciplina(self):
        '''
        Returneaza numele string disciplinei
        :return: string
        '''
        return self.__nume_disciplina

    def get_profesor_disciplina(self):
        '''
        Returneaza profesorul string care preda disciplina
        :return: string
        '''
        return self.__profesor_disciplina

    def set_nume_disciplina(self, nume_nou):
        '''
        Seteaza un nume nou disciplinei
        :param nume_nou: string
        :return: -
        '''
        self.__nume_disciplina = nume_nou

    def set_profesor_disciplina(self, profesor_nou):
        '''
        Seteaza un profesor nou disciplinei
        :param profesor_nou: string
        :return: -
        '''
        self.__profesor_disciplina = profesor_nou

    def __eq__(self, other):
        '''
        Verifica daca doua disciplpine sunt egale(prin id)
        :param other: disciplina
        :return: True daca idul disciplinei self = iddul disciplinei other
                 False altfel
        '''
        return self.__id_disciplina == other.__id_disciplina

    def __str__(self):
        '''
        Returneaza un string in care sunt precizate toate datele unei discipline
        :return: string
        '''
        return f"Disciplina [{self.__id_disciplina}] : Nume : {self.__nume_disciplina} Profesor : {self.__profesor_disciplina}"